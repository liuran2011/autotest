from constants import *

class Project(object):
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def conf_file(self):
        if self.type==NFC_INSTALL_TEST:
            return os.sep.join([PROJECTS_DIRECTORY,NFC_INSTALL_TEST_DIR,"conf",self.name])

