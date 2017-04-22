from ui_setting_project import Ui_settingProjectDialog
from PyQt5.QtWidgets import QDialog
from nfc_setting import NFCSetting

class SettingProject(QDialog,Ui_settingProjectDialog):
    def __init__(self,parent=None):
        super(SettingProject,self).__init__(parent)

        self.setupUi(self)
        
        self.settingProjectButton.clicked.connect(self._setting_project)
        self.cancelSettingButton.clicked.connect(self.close)

    def _setting_project(self):
        nfc_setting=NFCSetting()
        nfc_setting.exec_()
