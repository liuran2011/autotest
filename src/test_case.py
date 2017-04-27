#coding=utf-8

from test_log import TestLog

class NotImplementionException(Exception):
    """not implemention exception"""

class TestCase(object):
    def __init__(self,project_name,project_type):
        self.project_name=project_name
        self.project_type=project_type
        self.log=TestLog(project_type,project_name)

    def close(self):
        self.log.close()

    def name(self):
        raise NotImplementionException("测试用例必须实现name()函数!")

    def vm_list(self):
        return []

    def has_vm(self):
        return False

    def run(self):
        raise NotImplementionException("测试用例必须实现run()函数!")
