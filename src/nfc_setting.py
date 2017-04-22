from ui_nfc_setting import Ui_nfcProjectSetting
from PyQt5.QtWidgets import QDialog

class NFCSetting(QDialog,Ui_nfcProjectSetting):
    def __init__(self,parent=None):
        super(NFCSetting,self).__init__(parent)

        self.setupUi(self)
        
        self.okButton.clicked.connect(self._nfc_setting)
        self.cancelButton.clicked.connect(self.close)

    def _nfc_setting(self):
        pass
