#coding=utf-8

from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from constants import *
from nfc_test_types import NFCTestTypes
from test_case_manager import TM

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

    def _vm_delete(self,project_name,project_type,vminfo):
        if not self._is_current_project(project_name,project_type):
            return
       
        for row in range(self._vm_row_count):
            if str(self.vmTableWidget.item(row,1).text())==vminfo.uuid():
                self.vmTableWidget.removeRow(row)
                self._vm_row_count=self._vm_row_count-1
                break
        
    def _vm_update(self,project_name,project_type,vminfo):
        if not self._is_current_project(project_name,project_type):
            return

    def _is_current_project(self,project_name,project_type):
        if (str(self.projectName.text())==project_name 
            and str(self.projectType.text())==project_type):
            return True

        return False

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

        item_key=QTableWidgetItem()
        item_key.setText(case)
       
        item_value=QTableWidgetItem()
        item_value.setText("正在执行...")

        self.testResultTreeWidget.insertRow(self._test_result_row_count)
        self.testResultTreeWidget.setItem(self._test_result_row_count,0,item_key) 
        self.testResultTreeWidget.setItem(self._test_result_row_count,1,item_value)
        self._test_result_row_count=self._test_result_row_count+1

        self.currentTest.setText(case)

    def _test_case_completed(self,project_name,project_type,case,result):
        if not self._is_current_project(project_name,project_type):
            return

        item=self.testResultTreeWidget.item(self.testResultTreeWidget.rowCount()-1,1)
        if result:
            item.setText("成功")
        else:
            item.setText("失败")

    def _start_test(self):
        version=str(self.version.text())
        if not version:
            QMessageBox.information(self,"提示","请输入测试版本!")
            return

        self._test_result_row_count=0
        self.startTestButton.setEnabled(False)
        self.stopTestButton.setEnabled(True)
        TM.start_test(str(self.projectType.text()),str(self.projectName.text()),version)

    def _stop_test(self):
        TM.stop_test(str(self.projectType.text()),str(self.projectName.text()))
        self.stopTestButton.setEnabled(False)
        self.startTestButton.setEnabled(True)
        self._test_result_row_count=0

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
            currentTest=currentTest if currentTest else ""
            startTime=TM.get_start_time(name,type)
            startTime=startTime if startTime else ""
            endTime=TM.get_end_time(name,type)
            endTime=endTime if endTime else ""

        self.projectName.setText(name)
        self.projectType.setText(type)
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
       
        """
        self.testResultTreeWidget.clear()
        """

        cases=TM.get_cases(name,type)
        for case,ret in cases.iteritems():
            item_case=QTableWidgetItem()
            item_ret=QTableWidgetItem()
            item_case.setText(case)

            if ret:
                item_ret.setText("成功")
            else:
                item_ret.setText("失败")

            row=self.testResultTreeWidget.rowCount()
            self.testResultTreeWidget.setItem(row,0,item_case)
            self.testResultTreeWidget.setItem(row,1,item_ret)
