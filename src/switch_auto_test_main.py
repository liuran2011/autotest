from ui_switch_auto_test_main import Ui_switchAutoTestMain
from PyQt5.QtWidgets import QWidget

class SwitchAutoTestMain(QWidget,Ui_switchAutoTestMain):
    def __init__(self,parent=None):
        super(SwitchAutoTestMain,self).__init__(parent)

        self.setupUi(self)

    def update_project(self,project):
        pass
