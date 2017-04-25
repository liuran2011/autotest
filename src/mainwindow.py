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
from test_case_manager import TM

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)

        self.setupUi(self)
        self._setup_actions()

        self._setup_central_widget()

        self._setup_project_types()
        self._update_projects()
        PM.add_observer(self,self._add_project_callback,
                        self._delete_project_callback,
                        self._modify_project_callback)
        self.treeWidget.expandAll()

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
    
    def _get_top_level_item(self,type): 
        item_count=self.treeWidget.topLevelItemCount()
        for index in range(0,item_count):
            top_level_item=self.treeWidget.topLevelItem(index)
            if str(top_level_item.text(0))==type:
                return top_level_item

        return None

    def _get_project_item(self,top_level_item,name):
        count=top_level_item.childCount()
        for index in range(0,count):
            item=top_level_item.child(index)
            if str(item.text(0))==name:
                return item

        return None

    def _modify_project_callback(self,name,type):
        if self._current_widget_type!=type:
            return

        top_level_item=self._get_top_level_item(type)
        project_item=self._get_project_item(top_level_item,name)
        if project_item==self.treeWidget.currentItem():
            self._project_widget_show(type,name)
        
    def _delete_project_callback(self,name,type):
        top_level_item=self._get_top_level_item(type)
        project_item=self._get_project_item(top_level_item,name)
        current_item=self.treeWidget.currentItem()
        if project_item:
            top_level_item.removeChild(project_item)
        
        if self._current_widget_type!=type:
            return

        if current_item!=project_item:
            return

        if top_level_item.childCount():
            item=top_level_item.child(0)
            self.treeWidget.setCurrentItem(item)
            self._project_widget_show(type,str(item.text(0)))
        else:
            self._project_widget_show(type,None)
 
    def _add_project_callback(self,name,type):
        top_level_item=self._get_top_level_item(type)
        item=QTreeWidgetItem(top_level_item)
        item.setText(0,name)

    def _clear_top_level_item_children(self,top_level_item):
        while top_level_item.childCount():
            top_level_item.removeChild(top_level_item.child(0))
            
    def _update_projects_by_type(self,type):
        top_level_item=self._get_top_level_item(type)
        self._clear_top_level_item_children(top_level_item)

        projects=PM.project_list(type)
        for project in projects:
            item=QTreeWidgetItem(top_level_item)
            item.setText(0,project.name)
         
    def _update_projects(self):
        item_count=self.treeWidget.topLevelItemCount()
        for index in range(0,item_count):
            top_level_item=self.treeWidget.topLevelItem(index)
           
            type=str(top_level_item.text(0)) 
            self._update_projects_by_type(type)
 
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
            self.centralGridLayout.removeWidget(self._project_type_widget_dict[self._current_widget_type])
            self._current_widget_type=None
        
        project_name=None
        item=self.treeWidget.currentItem()
        if item.parent():
            project_name=str(item.text(0))
            item=item.parent()

        type=str(item.text(0))
        self.centralGridLayout.addWidget(self._project_type_widget_dict[type])
        self._project_widget_show(type,project_name)
        self._current_widget_type=type

    def _setup_actions(self):
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionNewProject.triggered.connect(self._new_project_select)
        self.actionDeleteProject.triggered.connect(self._delete_project)
        self.actionSettingProject.triggered.connect(self._setting_project)
        
        self.actionAbout.triggered.connect(self._about_show)

        self.treeWidget.itemClicked.connect(self._central_widget_update)
