#coding=utf-8

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

    def test_log_directory(self,project_type):
        return os.path.join(PROJECTS_DIRECTORY,self.test_dir(project_type),"test_log")

    def test_dir(self,project_type):
        if project_type==NFC_INSTALL_TEST:
            return NFC_INSTALL_TEST_DIR
        elif project_type==NFC_AUTO_TEST:
            return NFC_AUTO_TEST_DIR
        elif project_type==CENI_INSTALL_TEST:
            return CENI_INSTALL_TEST_DIR
        elif project_type==CENI_AUTO_TEST:
            return CENI_AUTO_TEST_DIR
        elif project_type==SWITCH_AUTO_TEST:
            return SWITCH_AUTO_TEST_DIR
        else:
            raise ValueError("无效的项目类型:%s"%(project_type))

    def test_type(self,project_dir):
        if project_dir==NFC_INSTALL_TEST_DIR:
            return NFC_INSTALL_TEST
        elif project_dir==NFC_AUTO_TEST_DIR:
            return NFC_AUTO_TEST
        elif project_dir==CENI_INSTALL_TEST_DIR:
            return CENI_INSTALL_TEST
        elif project_dir==CENI_AUTO_TEST_DIR:
            return CENI_AUTO_TEST
        elif project_dir==SWITCH_AUTO_TEST_DIR:
            return SWITCH_AUTO_TEST
        else:
            raise ValueError("invalid project_dir:%s"%(project_dir))

ENV=Env()
