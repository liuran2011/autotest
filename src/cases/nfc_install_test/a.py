import time
from test_case_manager import TM
from vm_info import VMInfo
from test_case import TestCase

class Case(TestCase):
    def __init__(self,name,type):
        super(Case,self).__init__(name,type)
        self.vm_list=[]

    def name(self):
        return "test-case-a"
    
    def has_vm(self):
        return True

    def vm_list(self):
        return self.vm_list

    def run(self):
        self.log.info("create vm")
        vminfo1=VMInfo('a','1234','active','172.16.1.1')
        self.vm_list.append(vminfo1)
        TM.add_vm_notify(self.project_name,self.project_type,vminfo1)

        time.sleep(5)
        self.log.info("add vm2")
        vminfo2=VMInfo('b','466','buildig...','172.16.2.1')
        TM.add_vm_notify(self.project_name,self.project_type,vminfo2)
        self.vm_list.append(vminfo2)

        time.sleep(6)
        self.log.info("delete vm1")
        TM.delete_vm_notify(self.project_name,self.project_type,vminfo1)
        self.vm_list.remove(vminfo1)

        time.sleep(3)
        self.log.info("delete vm2")
        TM.delete_vm_notify(self.project_name,self.project_type,vminfo2)
        self.vm_list.remove(vminfo2) 
    
        self.log.info("test success")

        return True