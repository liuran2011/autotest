from ui_nfc_install_project import Ui_nfcInstallProjectDialog
from PyQt5.QtWidgets import QDialog

class NFCInstallProject(QDialog,Ui_nfcInstallProjectDialog):
    def __init__(self,parent=None):
        super(NFCInstallProject,self).__init__(parent)

        self.setupUi(self)

