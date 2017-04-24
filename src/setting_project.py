# -*- coding: utf-8 -*-

from ui_setting_project import Ui_settingProjectDialog
from PyQt5.QtWidgets import QDialog,QListWidgetItem,QMessageBox
from nfc_setting import NFCSetting
from config import CONF
from project_manager import PM
from constants import *

class SettingProject(QDialog,Ui_settingProjectDialog):
    def __init__(self,parent=None):
        super(SettingProject,self).__init__(parent)

        self.setupUi(self)
        
        self._setup_project_type()
        
        self.settingProjectButton.clicked.connect(self._setting_project)
        self.cancelSettingButton.clicked.connect(self.close)
        self.comboBox.currentIndexChanged.connect(self._update_project_list)

    def _update_project_list(self):
        self._list_project(str(self.comboBox.currentText()))

    def _list_project(self,type):
        self.settingProjectList.clear()
        for project in PM.project_list(type):
            item=QListWidgetItem()
            item.setText(project.name)
            self.settingProjectList.addItem(item)
 
    def _setup_project_type(self):
        for type in CONF.project_type_list():
            self.comboBox.addItem(type)

        self.comboBox.setCurrentIndex(0)
        self._list_project(str(self.comboBox.currentText()))

    def _setting_project(self):
        item=self.settingProjectList.currentItem()
        if not item:
            QMessageBox.warning(self,"告警","请选择要设置的项目!")
            return

        name=str(item.text())
        type=str(self.comboBox.currentText())
        project=PM.get_project(name,type)
 
        if type==NFC_INSTALL_TEST:
            nfc_setting=NFCSetting(project)
            nfc_setting.exec_()
