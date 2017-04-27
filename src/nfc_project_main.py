#coding=utf-8

from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget,QMessageBox
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

        TM.add_observer(self,self._test_started,
                        self._test_stopped,self._test_case_started,
                        self._test_case_completed)

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

        item=QTableWidgetItem(self.testResultTreeWidget)
        item.setText(0,case)
        
        self.currentTest.setText(case)

    def _test_case_completed(self,project_name,project_type,case,result):
        if not self._is_current_project(project_name,project_type):
            return

        count=self.testResultTreeWidget.rowCount()
        for index in range(count):
            case_item=self.testResultTreeWidget.item(index,0)
            result_item=self.testResultTreeWidget.item(index,1)
            if str(case_item.text(0))==case:
                if result:
                    result_item.setText(1,"成功")
                else:
                    result_item.setText(1,"失败")
                break

    def _start_test(self):
        version=str(self.version.text())
        if not version:
            QMessageBox.information(self,"提示","请输入测试版本!")
            return

        self.startTestButton.setEnabled(False)
        self.stopTestButton.setEnabled(True)
        TM.start_test(str(self.projectType.text()),str(self.projectName.text()),version)

    def _stop_test(self):
        TM.stop_test(str(self.projectType.text()),str(self.projectName.text()))
        self.stopTestButton.setEnabled(False)
        self.startTestButton.setEnabled(True)

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
        while self.testResultTreeWidget.rowCount():
            self.testResultTreeWidget.removeRow(0)
        """

        cases=TM.get_cases(name,type)
        for case,ret in cases.iteritems():
            item=QTreeWidgetItem(self.testResultTreeWidget)
            item.setText(0,case)
            if ret:
                item.setText(1,"成功")
            else:
                item.setText(1,"失败")

