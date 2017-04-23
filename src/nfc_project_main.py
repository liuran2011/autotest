from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget
from constants import *
from nfc_test_types import NFCTestTypes

class NFCProjectMain(QWidget,Ui_nfcProjectForm):
    def __init__(self,parent=None):
        super(NFCProjectMain,self).__init__(parent)

        self.setupUi(self)
        self.projectType.setText(NFC_INSTALL_TEST)

        nfc_test_types=NFCTestTypes(self)
        self.verticalLayoutTest.insertWidget(0,nfc_test_types)
