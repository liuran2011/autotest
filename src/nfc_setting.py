from ui_nfc_setting import Ui_nfcProjectSetting
from PyQt5.QtWidgets import QDialog
from nfc_test_types import NFCTestTypes

class NFCSetting(QDialog,Ui_nfcProjectSetting):
    def __init__(self,parent=None):
        super(NFCSetting,self).__init__(parent)

        self.setupUi(self)
        
        self.okButton.clicked.connect(self._nfc_setting)
        self.cancelButton.clicked.connect(self.close)

        nfc_test_types=NFCTestTypes(self)
        self.verticalLayoutTest.insertWidget(self.verticalLayoutTest.count()-1,nfc_test_types)

    def _nfc_setting(self):
        pass
