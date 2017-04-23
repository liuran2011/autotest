from ui_nfc_project_main import Ui_nfcProjectForm
from PyQt5.QtWidgets import QWidget
from constants import *

class NFCProjectMain(QWidget,Ui_nfcProjectForm):
    def __init__(self,parent=None):
        super(NFCProjectMain,self).__init__(parent)

        self.setupUi(self)
        self.projectType.setText(NFC_INSTALL_TEST)
