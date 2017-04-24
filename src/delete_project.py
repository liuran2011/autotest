# -*- coding: utf-8 -*-

from ui_delete_project import Ui_deleteProjectDialog
from PyQt5.QtWidgets import QDialog,QListWidgetItem,QMessageBox
from config import CONF
from project_manager import PM

class DeleteProject(QDialog,Ui_deleteProjectDialog):
    def __init__(self,parent=None):
        super(DeleteProject,self).__init__(parent)

        self.setupUi(self)

        self._setup_project_type_list()
        
        self.deleteProjectButton.clicked.connect(self._delete_project)
        self.cancelDeleteProjectButton.clicked.connect(self.close)
        self.comboBox.currentIndexChanged.connect(self._update_project_list)

    def _setup_project_type_list(self):
        for type in CONF.project_type_list():
            self.comboBox.addItem(type)

        self.comboBox.setCurrentIndex(0)
        self._list_project(str(self.comboBox.currentText()))

    def _update_project_list(self):
        self._list_project(str(self.comboBox.currentText()))

    def _list_project(self,type):
        self.projectList.clear()
        for project in PM.project_list(type):
            item=QListWidgetItem()
            item.setText(project.name)
            self.projectList.addItem(item)
          
    def _delete_project(self):
        item=self.projectList.currentItem()
        if not item:
            QMessageBox.warning(self,"告警","请选择要删除的项目!")
            return
        
        name=str(item.text())
        type=str(self.comboBox.currentText())

        try:
            PM.delete_project(name,type)
        except Exception as e:
            QMessageBox.warning(self,"告警","删除项目:%s 类型:%s 失败，异常:%s"%(name,type,e))
            return

        QMessageBox.information(self,"提示","删除项目成功!")
        self.close()
