from ui_nfc_auto_test_main import Ui_nfcAutoTestMain
from PyQt5.QtWidgets import QWidget

class NFCAutoTestMain(QWidget,Ui_nfcAutoTestMain):
    def __init__(self,parent=None):
        super(NFCAutoTestMain,self).__init__(parent)

        self.setupUi(self)
