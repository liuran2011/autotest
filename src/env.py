from constants import *
import os

class Env(object):
    def __init__(self):
        self._init_top_level_dir()
        self._init_projects_dir()

    def _init_top_level_dir(self):
        top_level_dir_list=[CONFIG_DIRECTORY,
                            PROJECTS_DIRECTORY,
                            LOG_DIRECTORY]
        for dir in top_level_dir_list:
            if not os.path.exists(dir):
                os.makedirs(dir)

    def _init_project_conf_dir(self,path):
        dir=os.sep.join([path,"conf"])
        if not os.path.exists(dir):
            os.makedirs(dir)

    def _init_project_test_log_dir(self,path):
        dir=os.sep.join([path,"test_log"])
        if not os.path.exists(dir):
            os.makedirs(dir)
 
    def _init_projects_dir(self):
        for dir in AUTO_TEST_PROJECT_DIR_LIST:
            path=os.sep.join([PROJECTS_DIRECTORY,dir])
            if not os.path.exists(path):
                os.makedirs(path)
                
                self._init_project_conf_dir(path)
                self._init_project_test_log_dir(path)
   
    def conf_file(self):
        return CONFIG_FILE

ENV=Env()
