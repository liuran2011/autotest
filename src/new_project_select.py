from ui_new_project_select import Ui_newProjectSelect
from PyQt5.QtWidgets import QDialog
from nfc_install_project import NFCInstallProject

class NewProjectSelect(QDialog,Ui_newProjectSelect):
    def __init__(self,parent=None):
        super(NewProjectSelect,self).__init__(parent)

        self.setupUi(self)
        
        self.okButton.clicked.connect(self._new_project)
        self.cancelButton.clicked.connect(self.close)

    def _new_project(self):
        nfc_install=NFCInstallProject()
        nfc_install.exec_()        
