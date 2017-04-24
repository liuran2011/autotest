from constants import *
from bk_nfc_install_project import BKNFCInstallProject

class ProjectFactory(object):
    def create_project(self,name,type,**kwargs):
        project=None
        if type==NFC_INSTALL_TEST:
            project=BKNFCInstallProject(name,type,**kwargs)
            project.save()
            return project

        return project

    def load_project(self,conf_file,type):
        if type==NFC_INSTALL_TEST:
             return BKNFCInstallProject.load(conf_file)

        return None

    def delete_project(self,project):
        if project.type==NFC_INSTALL_TEST:
            BKNFCInstallProject.delete(project)

    def modify_project(self,project,**kwargs):
        project.modify(**kwargs)

PF=ProjectFactory()
