from PyQt5.QtWidgets import QGridLayout,QApplication,QMainWindow,QTreeWidgetItem
from ui_mainwindow import Ui_MainWindow
from about_dialog import AboutDialog
from new_project_select import NewProjectSelect
from delete_project import DeleteProject
from setting_project import SettingProject
from nfc_project_main import NFCProjectMain
from switch_auto_test_main import SwitchAutoTestMain
from nfc_auto_test_main import NFCAutoTestMain
from ceni_install_main import CENIInstallMain
from ceni_auto_test_main import CENIAutoTestMain
from config import CONF
from constants import *
from project_manager import PM

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._setup_actions()

        self._setup_central_widget()

        self._setup_project_types()
        self._update_projects()

    def _setup_central_widget(self):
        self.centralGridLayout=QGridLayout(self.centralWidget)
        self.centralGridLayout.setObjectName("centralGridLayout")

        self._current_widget_type=None
 
    def _setup_project_types(self):
        type_widget_map={
                            NFC_INSTALL_TEST:NFCProjectMain,
                            NFC_AUTO_TEST:NFCAutoTestMain,
                            CENI_INSTALL_TEST:CENIInstallMain,
                            CENI_AUTO_TEST:CENIAutoTestMain,
                            SWITCH_AUTO_TEST:SwitchAutoTestMain
                        }
        self._project_type_widget_dict={}
        types=CONF.project_type_list()
        for type in types:
            item=QTreeWidgetItem(self.treeWidget)
            item.setText(0,type)
          
            self._project_type_widget_dict[type]=type_widget_map[type]() 
            
    def _update_projects(self):
        item_count=self.treeWidget.topLevelItemCount()
        for index in range(0,item_count):
            top_level_item=self.treeWidget.topLevelItem(index)
           
            type=str(top_level_item.text(0)) 
            projects=PM.project_list(type)
            for project in projects:
                item=QTreeWidgetItem(top_level_item)
                item.setText(0,project.name)
 
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
    
    def _project_widget_show(self,project_type,project_name):
        for type in self._project_type_widget_dict:
            self._project_type_widget_dict[type].hide()

        self._project_type_widget_dict[project_type].update_project(PM.get_project(project_name,project_type))
        self._project_type_widget_dict[project_type].show()

    def _central_widget_update(self):
        if self._current_widget_type:
            self.centralGridLayout.removeWidget(self._project_type_widget_dict[type])
            self._current_widget_type=None
        
        project_name=None
        item=self.treeWidget.currentItem()
        if item.parent():
            project_name=str(item.text(0))
            item=item.parent()

        type=str(item.text(0))
        self.centralGridLayout.addWidget(self._project_type_widget_dict[type])
        self._project_widget_show(type,project_name)

    def _setup_actions(self):
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionNewProject.triggered.connect(self._new_project_select)
        self.actionDeleteProject.triggered.connect(self._delete_project)
        self.actionSettingProject.triggered.connect(self._setting_project)
        
        self.actionAbout.triggered.connect(self._about_show)

        self.treeWidget.itemClicked.connect(self._central_widget_update)
