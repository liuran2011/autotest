from ui_new_project_select import Ui_newProjectSelect
from PyQt5.QtWidgets import QDialog,QListWidgetItem
from nfc_install_project import NFCInstallProject
from config import CONF
from constants import *

class NewProjectSelect(QDialog,Ui_newProjectSelect):
    def __init__(self,parent=None):
        super(NewProjectSelect,self).__init__(parent)

        self.setupUi(self)
       
        self.okButton.clicked.connect(self._new_project)
        self.cancelButton.clicked.connect(self.close)

        self._setup_list()

    def _nfc_install_test(self):
        self.hide()
        nfc_install=NFCInstallProject()
        nfc_install.projectType.setText(NFC_INSTALL_TEST)
        nfc_install.exec_()
    
    def _new_project(self):
        if str(self.listWidget.currentItem().text())==NFC_INSTALL_TEST:
            self._nfc_install_test()
 
    def _setup_list(self):
        types=CONF.project_type_list()
        for type in types:
            item=QListWidgetItem()
            item.setText(type)
            self.listWidget.addItem(item) 
