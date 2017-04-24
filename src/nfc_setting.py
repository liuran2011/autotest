#coding=utf-8

from ui_nfc_setting import Ui_nfcProjectSetting
from PyQt5.QtWidgets import QDialog,QMessageBox
from nfc_test_types import NFCTestTypes
from project_manager import PM

class NFCSetting(QDialog,Ui_nfcProjectSetting):
    def __init__(self,project,parent=None):
        super(NFCSetting,self).__init__(parent)
        
        self.setupUi(self)
        
        self.okButton.clicked.connect(self._nfc_setting)
        self.cancelButton.clicked.connect(self.close)

        self.nfc_test_types=NFCTestTypes(self)
        self.verticalLayoutTest.insertWidget(self.verticalLayoutTest.count()-1,self.nfc_test_types)
        self._project=project

        self._setup_project_value()

    def _setup_project_value(self):
        if not self._project:
            return

        self.project.setText(self._project.name)
        self.tenant.setText(self._project.tenant)
        self.password.setText(self._project.password)
        self.nfc_test_types.set_selected_cases(self._project.cases)

    def _nfc_setting(self):
        tenant=str(self.tenant.text())
        password=str(self.password.text())
        cases=self.nfc_test_types.selected_test_types()
        if(len(tenant)==0 or len(password)==0):
            QMessageBox.information(self,"提示","租户和密码不能为空!")
            return

        if(len(cases)==0):
            QMessageBox.information(self,"提示","请选择测试类型!")
            return

        try:
            PM.modify_project(self._project.name,self._project.type,
                            tenant=tenant,password=password,cases=cases)
        except Exception as e:
            print e
            QMessageBox.warning(self,"提示","修改项目:%s 类型:%s 失败，异常:%s"(self._project.name,
                        self._project.type,e))
            return

        QMessageBox.information(self,"提示","设置项目成功!")
        self.close()
