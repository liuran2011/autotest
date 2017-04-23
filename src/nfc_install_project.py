from ui_nfc_install_project import Ui_nfcInstallProjectDialog
from PyQt5.QtWidgets import QDialog
from nfc_test_types import NFCTestTypes

class NFCInstallProject(QDialog,Ui_nfcInstallProjectDialog):
    def __init__(self,parent=None):
        super(NFCInstallProject,self).__init__(parent)

        self.setupUi(self)

        self.okButton.clicked.connect(self._ok)
        self.cancelButton.clicked.connect(self.close)

        nfc_test_types=NFCTestTypes(self)
        self.verticalLayout.insertWidget(self.verticalLayout.count()-1,nfc_test_types)

    def _ok(self):
        pass
