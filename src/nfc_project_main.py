#coding=utf-8

from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from constants import *
from nfc_test_types import NFCTestTypes
from test_case_manager import TM
import threading

class NFCProjectMain(QWidget,Ui_nfcProjectForm):
    def __init__(self,parent=None):
        super(NFCProjectMain,self).__init__(parent)

        self.setupUi(self)
        self.projectType.setText(NFC_INSTALL_TEST)

        self.nfc_test_types=NFCTestTypes(self)
        self.verticalLayoutTest.insertWidget(0,self.nfc_test_types)
        
        self.startTestButton.clicked.connect(self._start_test)
        self.stopTestButton.clicked.connect(self._stop_test)
        
        self.startTestButton.setEnabled(True)
        self.stopTestButton.setEnabled(False)

        self._test_result_lock=threading.Lock()
        self._vm_list_lock=threading.Lock()
        self._test_result_row_count=0
        self._vm_row_count=0

        TM.add_observer(self,self._test_started,
                        self._test_stopped,self._test_case_started,
                        self._test_case_completed)
        TM.add_vm_observer(self,
                        self._vm_add,
                        self._vm_delete,
                        self._vm_update)

    def _vm_add(self,project_name,project_type,vminfo):
        if not self._is_current_project(project_name,project_type):
            return

        self._vm_list_lock.acquire()
        self._insert_vm_row(vminfo)
        self._vm_list_lock.release()

    def _vm_delete(self,project_name,project_type,vminfo):
        if not self._is_current_project(project_name,project_type):
            return
      
        self._vm_list_lock.acquire()
        for row in range(self._vm_row_count):
            item=self.vmTableWidget.item(row,1)
            if item and str(item.text())==vminfo.uuid():
                self.vmTableWidget.removeRow(row)
                self._vm_row_count=self._vm_row_count-1
                break
        self._vm_list_lock.release()

    def _vm_update(self,project_name,project_type,vminfo):
        if not self._is_current_project(project_name,project_type):
            return
        
        self._vm_list_lock.acquire()
        self._vm_list_lock.release()

    def _is_current_project(self,project_name,project_type):
        if (str(self.projectName.text())==project_name 
            and str(self.projectType.text())==project_type):
            return True

        return False

    def _vm_list_clear_rows(self):
        self._vm_list_lock.acquire()
        self._vm_row_count=0
        while self.vmTableWidget.rowCount():
            self.vmTableWidget.removeRow(0)
        self._vm_list_lock.release()

    def _test_result_clear_rows(self):
        self._test_result_lock.acquire()
        while self.testResultTreeWidget.rowCount():
            self.testResultTreeWidget.removeRow(0)
        self._test_result_row_count=0
        self._test_result_lock.release()

    def _test_started(self,project_name,project_type,time):
        if not self._is_current_project(project_name,project_type):
            return

        self.startTestTime.setText(time)

    def _test_stopped(self,project_name,project_type,time):
        if not self._is_current_project(project_name,project_type):
            return

        self.endTestTime.setText(time)
        self.stopTestButton.setEnabled(False)
        self.startTestButton.setEnabled(True)
        
    def _test_case_started(self,project_name,project_type,case):
        if not self._is_current_project(project_name,project_type):
            return

        self._test_result_lock.acquire()
        self._insert_test_result_row(case,"正在执行...")
        self._test_result_lock.release()

        self.currentTest.setText(case)

    def _test_case_completed(self,project_name,project_type,case,result):
        if not self._is_current_project(project_name,project_type):
            return

        self._test_result_lock.acquire()
        if self.testResultTreeWidget.rowCount():
            item=self.testResultTreeWidget.item(self.testResultTreeWidget.rowCount()-1,1)
            if result:
                item.setText("成功")
            else:
                item.setText("失败")
        self._test_result_lock.release()

    def _start_test(self):
        version=str(self.version.text())
        if not version:
            QMessageBox.information(self,"提示","请输入测试版本!")
            return

        self.startTestButton.setEnabled(False)
        self.stopTestButton.setEnabled(True)

        TM.stop_test(str(self.projectType.text()),str(self.projectName.text()))
        
        self._vm_list_clear_rows()
        self._test_result_clear_rows()

        TM.start_test(str(self.projectType.text()),str(self.projectName.text()),version)

    def _stop_test(self):
        TM.stop_test(str(self.projectType.text()),str(self.projectName.text()))
        self.stopTestButton.setEnabled(False)
        self.startTestButton.setEnabled(True)
        self._test_result_row_count=0

    def _insert_test_result_row(self,case,ret):
        self.testResultTreeWidget.insertRow(self._test_result_row_count)
        item_case=QTableWidgetItem()
        item_result=QTableWidgetItem()
        item_case.setText(case)
        item_result.setText(ret)
        self.testResultTreeWidget.setItem(self._test_result_row_count,0,item_case)
        self.testResultTreeWidget.setItem(self._test_result_row_count,1,item_result)
        self._test_result_row_count=self._test_result_row_count+1

    def _test_result_update(self,name,type):
        self._test_result_lock.acquire()
        cases=TM.get_cases(str(name),str(type))

        for case,ret in cases.iteritems():
            if ret==True:
                result="成功"
            elif ret==None:
                result="正在执行..."
            else:
                result="失败"
            self._insert_test_result_row(case,result)            
        self._test_result_lock.release()

    def _insert_vm_row(self,vminfo):
        self.vmTableWidget.insertRow(self._vm_row_count)
        
        item_name=QTableWidgetItem()
        item_uuid=QTableWidgetItem()
        item_status=QTableWidgetItem()
        item_floating_ip=QTableWidgetItem()
        item_name.setText(vminfo.name())
        item_uuid.setText(vminfo.uuid())
        item_status.setText(vminfo.status())
        item_floating_ip.setText(vminfo.floating_ip())
        
        self.vmTableWidget.setItem(self._vm_row_count,0,item_name)
        self.vmTableWidget.setItem(self._vm_row_count,1,item_uuid)
        self.vmTableWidget.setItem(self._vm_row_count,2,item_status)
        self.vmTableWidget.setItem(self._vm_row_count,3,item_floating_ip)

        self._vm_row_count=self._vm_row_count+1

    def _vm_list_update(self,name,type):
        self._vm_list_lock.acquire()
        case=TM.get_current_test(name,type)
        if case and case.has_vm():
            for vminfo in  case.virtual_machine_list():
                self._insert_vm_row(vminfo)
        self._vm_list_lock.release()

    def update_project(self,project):
        if not project:
            name=""
            type=""
            keystone_url=""
            region=""
            tenant=""
            password=""
            public_network=""
            cases=[]
            version=""
            currentTest=""
            startTime=""
            endTime=""
        else:
            name=project.name
            type=project.type
            keystone_url=project.keystone_url
            region=project.region
            tenant=project.tenant
            password=project.password
            public_network=project.public_network
            cases=project.cases
            version=TM.get_version(name,type)
            version=version if version else ""
            currentTest=TM.get_current_test(name,type)
            currentTest=currentTest.name() if currentTest else ""
            startTime=TM.get_start_time(name,type)
            startTime=startTime if startTime else ""
            endTime=TM.get_end_time(name,type)
            endTime=endTime if endTime else ""

        self.keystoneURL.setText(keystone_url)
        self.regionName.setText(region)
        self.tenant.setText(tenant)
        self.password.setText(password)
        self.publicNetwork.setText(public_network)
        self.nfc_test_types.set_selected_cases(cases)
        self.version.setText(version)
        self.currentTest.setText(currentTest)
        self.startTestTime.setText(startTime)
        self.endTestTime.setText(endTime)

        if TM.test_running(type,name):
            self.startTestButton.setEnabled(False)
            self.stopTestButton.setEnabled(True)
        else:
            self.startTestButton.setEnabled(True)
            self.stopTestButton.setEnabled(False)

        self._test_result_clear_rows()
        self._vm_list_clear_rows()

        if name and type:
            self._test_result_update(name,type)
            self._vm_list_update(name,type)

        self.projectName.setText(name)
        self.projectType.setText(type)
