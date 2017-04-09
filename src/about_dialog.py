from ui_about import Ui_aboutDialog
from PyQt5.QtWidgets import QDialog

class AboutDialog(QDialog,Ui_aboutDialog):
    def __init__(self,parent=None):
        super(AboutDialog,self).__init__(parent)
        
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)
