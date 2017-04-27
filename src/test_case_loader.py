import os
from env import ENV
import time
from log import LOG
import importlib
from constants import *

class TestCaseLoader(object):
    def _test_case_directory(self,type,name):
        return os.path.join(CASES_DIRECTORY,ENV.test_dir(type))

    def load_cases(self,type,name):
        cases=[]

        for parent_dir,dirnames,filenames in os.walk(self._test_case_directory(type,name)):
            for file in filenames:
                if file=="__init__.py":
                    continue

                if not file.endswith(".py"):
                    continue

                module_name="%s.%s.%s"%("cases",ENV.test_dir(type),file.strip(".py"))
                try:
                    module=importlib.import_module(module_name)
                except Exception as e:
                    LOG.error("import module: %s directory:%s failed. except:%s"%(file,parent_dir,e))
                    continue

                cases.append(module.Case(name,type))

        return cases

TL=TestCaseLoader()

