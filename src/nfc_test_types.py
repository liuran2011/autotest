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
        
        self._check_box_list=[]
        for type in CONF.nfc_test_list():
            btn=QCheckBox(self.groupBox)
            btn.setText(type)
            self._check_box_list.append(btn)
            self.verticalLayout.addWidget(btn) 

    def set_selected_cases(self,cases):
        for box in self._check_box_list:
            box.setChecked(False)

        for case in cases:
            for box in self._check_box_list:
                if str(box.text())==case:
                    box.setChecked(True)
                    break

    def selected_test_types(self):
        type_list=[]
        for box in self._check_box_list:
            if box.isChecked():
                type_list.append(str(box.text()))
        
        return type_list
