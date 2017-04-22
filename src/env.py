from constants import *
import os

class Env(object):
    def __init__(self):
        if not os.path.exists(CONFIG_DIRECTORY):
            os.makedirs(CONFIG_DIRECTORY)

        if not os.path.exists(PROJECTS_DIRECTORY):
            os.makedirs(PROJECTS_DIRECTORY)
    
        if not os.path.exists(TESTLOG_DIRECTORY):
            os.makedirs(TESTLOG_DIRECTORY)

        if not os.path.exists(LOG_DIRECTORY):
            os.makedirs(LOG_DIRECTORY)

    def conf_file(self):
        return CONFIG_FILE

ENV=Env()
