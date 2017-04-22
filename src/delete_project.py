from ui_delete_project import Ui_deleteProjectDialog
from PyQt5.QtWidgets import QDialog

class DeleteProject(QDialog,Ui_deleteProjectDialog):
    def __init__(self,parent=None):
        super(DeleteProject,self).__init__(parent)

        self.setupUi(self)
        
        self.deleteProjectButton.clicked.connect(self._delete_project)
        self.cancelDeleteProjectButton.clicked.connect(self.close)

    def _delete_project(self):
        pass
