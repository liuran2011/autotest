from ui_delete_project import Ui_deleteProjectDialog
from PyQt5.QtWidgets import QDialog
from config import CONF

class DeleteProject(QDialog,Ui_deleteProjectDialog):
    def __init__(self,parent=None):
        super(DeleteProject,self).__init__(parent)

        self.setupUi(self)

        self._setup_project_type_list()
        
        self.deleteProjectButton.clicked.connect(self._delete_project)
        self.cancelDeleteProjectButton.clicked.connect(self.close)

    def _setup_project_type_list(self):
        pass
 
    def _delete_project(self):
        pass
