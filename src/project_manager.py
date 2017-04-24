from constants import *
from log import LOG
from project_factory import PF
from env import ENV

class ProjectManager(object):
    def __init__(self):
        self._project_list=[]
        self._observer_list=[]
        
        self._reload_projects()

    def _reload_projects(self):
        for dir in AUTO_TEST_PROJECT_DIR_LIST:
            type=ENV.test_type(dir)
            conf_dir=os.sep.join([PROJECTS_DIRECTORY,dir,"conf"])
            
            for parent_dir,dirnames,filenames in os.walk(conf_dir):
                for file in filenames:
                    self._project_list.append(PF.load_project(os.path.join(parent_dir,file),type))

    def add_observer(self,obj,add_project,delete_project,modify_project):
        for o in self._observer_list:
            if o['object']==obj:
                return

        self._observer_list.append({'object':obj,
                        'add_project':add_project,
                        'delete_project':delete_project,
                        'modify_project':modify_project})

    def project_list(self,type):
        l=[]
        for project in self._project_list:
            if project.type==type:
                l.append(project)

        return l

    def project_exists(self,name,type):
        for project in self._project_list:
            if project.type==type and project.name==name:
                return True
        
        return False

    def add_project(self,name,type,**kwargs):
        if self.project_exists(name,type):
            return

        project=PF.create_project(name,type,**kwargs)
        self._project_list.append(project)
        self._add_project_notify(name,type)

    def get_project(self,name,type):
        for p in self._project_list:
            if p.type==type and p.name==name:
                return p
        
        return None 

    def modify_project(self,name,type,**kwargs):
        project=self.get_project(name,type)
        if project:
            PF.modify_project(project,**kwargs)
        self._modify_project_notify(name,type)
         
    def _notify(self,name,type,func):
        for observer in self._observer_list:
            observer[func](name,type)

    def _modify_project_notify(self,name,type):
        self._notify(name,type,'modify_project')

    def _add_project_notify(self,name,type):
        self._notify(name,type,'add_project')

    def _delete_project_notify(self,name,type):
        self._notify(name,type,'delete_project')
    
    def delete_project(self,name,type):
        p=self.get_project(name,type)
        if p:
            PF.delete_project(p)
            self._project_list.remove(p)
        
        self._delete_project_notify(name,type)
      
PM=ProjectManager()
