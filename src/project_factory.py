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

PF=ProjectFactory()
