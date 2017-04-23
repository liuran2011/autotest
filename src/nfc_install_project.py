# -*- coding: utf-8 -*-

from ui_nfc_install_project import Ui_nfcInstallProjectDialog
from PyQt5.QtWidgets import QDialog,QMessageBox
from nfc_test_types import NFCTestTypes
from project_manager import PM

class NFCInstallProject(QDialog,Ui_nfcInstallProjectDialog):
    def __init__(self,parent=None):
        super(NFCInstallProject,self).__init__(parent)

        self.setupUi(self)

        self.okButton.clicked.connect(self._ok)
        self.cancelButton.clicked.connect(self.close)

        nfc_test_types=NFCTestTypes(self)
        self.verticalLayout.insertWidget(self.verticalLayout.count()-1,nfc_test_types)

    def _ok(self):
        project_name=str(self.projectName.text())
        project_type=str(self.projectType.text())
        if PM.project_exists(project_name,project_type):
            QMessageBox().warning(self,"告警","项目:%s 类型:%s 已经存在!"%(project_name,project_type))
            return

        PM.add_project(project_name,project_type,
                        tenant=str(self.tenantName.text()),
                        password=str(self.password.text()),
                        keystone_url=str(self.keystoneURL.text()),
                        region=str(self.regionName.text()),
                        public_network=str(self.publicNetwork.text()))
