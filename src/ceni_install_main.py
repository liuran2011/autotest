from ui_ceni_install_main import Ui_ceniInstallMain
from PyQt5.QtWidgets import QWidget

class CENIInstallMain(QWidget,Ui_ceniInstallMain):
    def __init__(self,parent=None):
        super(CENIInstallMain,self).__init__(parent)

        self.setupUi(self)

    def update_project(self,project):
        pass
