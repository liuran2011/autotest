from PyQt5.QtWidgets import QGridLayout,QApplication,QMainWindow,QTreeWidgetItem
from ui_mainwindow import Ui_MainWindow
from about_dialog import AboutDialog
from new_project_select import NewProjectSelect
from delete_project import DeleteProject
from setting_project import SettingProject
from nfc_project_main import NFCProjectMain
from config import CONF
from constants import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._setup_actions()

        self._setup_central_widget()

        self._setup_project_types()
        self._setup_projects()

    def _setup_central_widget(self):
        self.centralGridLayout=QGridLayout(self.centralWidget)
        self.centralGridLayout.setObjectName("centralGridLayout")

        self._current_central_widget=None
 
    def _setup_project_types(self):
        self._project_type_widget_dict={}
        types=CONF.project_type_list()
        for type in types:
            item=QTreeWidgetItem(self.treeWidget)
            item.setText(0,type)
           
            if type==NFC_INSTALL_TEST:
                self._project_type_widget_dict[type]=NFCProjectMain()

    def _setup_projects(self):
        pass

    def _about_show(self):
        about=AboutDialog()
        about.exec_()

    def _new_project_select(self):
        new_pro=NewProjectSelect()
        new_pro.exec_()

    def _delete_project(self):
        del_pro=DeleteProject()
        del_pro.exec_()

    def _setting_project(self):
        setting=SettingProject()
        setting.exec_()
        
    def _central_widget_update(self):
        if not self._current_central_widget:
            self.centralGridLayout.removeWidget(self._current_central_widget)
            self._current_central_widget=None

        type=self.treeWidget.currentItem().text(0)
        widget=self._project_type_widget_dict.get(str(type),None)
        if widget:
            self.centralGridLayout.addWidget(widget)

    def _setup_actions(self):
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionNewProject.triggered.connect(self._new_project_select)
        self.actionDeleteProject.triggered.connect(self._delete_project)
        self.actionSettingProject.triggered.connect(self._setting_project)
        
        self.actionAbout.triggered.connect(self._about_show)

        self.treeWidget.itemClicked.connect(self._central_widget_update)
