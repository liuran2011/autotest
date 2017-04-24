from project_manager import PM
from log import LOG
from constants import *

class TestCaseManager(object):
    def __init__(self):
        PM.add_observer(self,
                        self._add_project_callback,
                        self._delete_project_callback,
                        self._modify_project_callback)
        self._test_cases={}

    def _add_project_callback(self,name,type):
        pass

    def _delete_project_callback(self,name,type):
        pass

    def _modify_project_callback(self,name,type):
        pass

    def start_test(self,project_type,project_name):
                
        pass

    def stop_test(self,project_type,project_name):
        pass
 
    def cases_status(self,project_type,project_name):
        pass        

TM=TestCaseManager()
