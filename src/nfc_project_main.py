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
            name=""
            type=""
            keystone_url=""
            region=""
            tenant=""
            password=""
            public_network=""
            cases=[]
        else:
            name=project.name
            type=project.type
            keystone_url=project.keystone_url
            region=project.region
            tenant=project.tenant
            password=project.password
            public_network=project.public_network
            cases=project.cases

        self.projectName.setText(name)
        self.projectType.setText(type)
        self.keystoneURL.setText(keystone_url)
        self.regionName.setText(region)
        self.tenant.setText(tenant)
        self.password.setText(password)
        self.publicNetwork.setText(public_network)
        self.nfc_test_types.set_selected_cases(cases)

