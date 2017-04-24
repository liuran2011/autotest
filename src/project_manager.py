from constants import *
from log import LOG
from project_factory import PF
from env import ENV

class ProjectManager(object):
    def __init__(self):
        self._project_list=[]
        
        self._reload_projects()

    def _reload_projects(self):
        for dir in AUTO_TEST_PROJECT_DIR_LIST:
            type=ENV.test_type(dir)
            conf_dir=os.sep.join([PROJECTS_DIRECTORY,dir,"conf"])
            
            for parent_dir,dirnames,filenames in os.walk(conf_dir):
                for file in filenames:
                    self._project_list.append(PF.load_project(os.path.join(parent_dir,file),type))

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

    def get_project(self,name,type):
        for p in self._project_list:
            if p.type==type and p.name==name:
                return p
        
        return None 

    def modify_project(self,name,type,**kwargs):
        project=self.get_project(name,type)
        if project:
            PF.modify_project(project,**kwargs)
 
    def delete_project(self,name,type):
        p=self.get_project(name,type)
        if p:
            PF.delete_project(p)
            self._project_list.remove(p)
        
PM=ProjectManager()
