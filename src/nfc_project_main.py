from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget
from constants import *
from nfc_test_types import NFCTestTypes

class NFCProjectMain(QWidget,Ui_nfcProjectForm):
    def __init__(self,parent=None):
        super(NFCProjectMain,self).__init__(parent)

        self.setupUi(self)
        self.projectType.setText(NFC_INSTALL_TEST)

        self.nfc_test_types=NFCTestTypes(self)
        self.verticalLayoutTest.insertWidget(0,self.nfc_test_types)

    def update_project(self,project):
        if not project:
            return

        self.projectName.setText(project.name)
        self.projectType.setText(project.type)
        self.keystoneURL.setText(project.keystone_url)
        self.regionName.setText(project.region)
        self.tenant.setText(project.tenant)
        self.password.setText(project.password)
        self.publicNetwork.setText(project.public_network)
        self.nfc_test_types.set_selected_cases(project.cases)

