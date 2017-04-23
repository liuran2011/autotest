from constants import *
from log import LOG
from project_factory import PF

class ProjectManager(object):
    def __init__(self):
        self._project_list=[]
        
        self._reload_projects()

    def _reload_projects(self):
        pass
    
    def project_list(self):
        return self._project_list

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
 
    def delete_project(self,project_name):
        pass        

PM=ProjectManager()
