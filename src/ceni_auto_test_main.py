from ui_ceni_auto_test_main import Ui_ceniAutoTestMain
from PyQt5.QtWidgets import QWidget

class CENIAutoTestMain(QWidget,Ui_ceniAutoTestMain):
    def __init__(self,parent=None):
        super(CENIAutoTestMain,self).__init__(parent)

        self.setupUi(self)
