from PyQt5.QtWidgets import QApplication,QMainWindow
from ui_mainwindow import Ui_MainWindow
from about_dialog import AboutDialog
from new_project_select import NewProjectSelect
from delete_project import DeleteProject
 
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._setup_actions()

    def _about_show(self):
        about=AboutDialog()
        about.exec_()

    def _new_project_select(self):
        new_pro=NewProjectSelect()
        new_pro.exec_()

    def _delete_project(self):
        del_pro=DeleteProject()
        del_pro.exec_()
        
    def _setup_actions(self):
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionNewProject.triggered.connect(self._new_project_select)
        self.actionDeleteProject.triggered.connect(self._delete_project)
        
        self.actionAbout.triggered.connect(self._about_show)
