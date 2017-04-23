from PyQt5.QtWidgets import QVBoxLayout,QWidget,QCheckBox
from ui_nfc_test_types import Ui_nfcTestTypes
from config import CONF

class NFCTestTypes(QWidget,Ui_nfcTestTypes):
    def __init__(self,parent=None):
        super(NFCTestTypes,self).__init__(parent)

        self.setupUi(self)
        self._setup_vertical_layout()

    def _setup_vertical_layout(self):
        self.verticalLayout=QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        
        for type in CONF.nfc_test_list():
            btn=QCheckBox(self.groupBox)
            btn.setText(type)
            self.verticalLayout.addWidget(btn) 
