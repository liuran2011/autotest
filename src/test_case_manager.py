from project_manager import PM
from log import LOG
from constants import *
import time
import threading
from test_case_loader import TL

class TestCaseManager(object):
    def __init__(self):
        PM.add_observer(self,
                        self._add_project_callback,
                        self._delete_project_callback,
                        self._modify_project_callback)
        
        """
        self._test_cases format:
        {   project_type:
            {   project_name:
                { thread: thread_object,version:version,stop_flag:True,current_case:case_name,
                  stime:start_time,etime:end_time,
                  cases:
                  { case:result}
                }
            }
        }
        """
        self._test_cases={}
        self._observer_list=[]
        
    def destroy(self):
        for type,projects in self._test_cases.iteritems():
            for name,project in projects.iteritems():
                if project['thread'].isAlive():
                    project['thread'].stop_flag=True
                    project['thread'].join()
                
    def add_observer(self,
                    object,
                    test_started,
                    test_stopped,
                    test_case_started,
                    test_case_completed):
        for o in self._observer_list:
            if o['object']==object:
                return

        self._observer_list.append({'object':object,
                    'test_started':test_started,
                    'test_stopped':test_stopped,
                    'test_case_started':test_case_started,
                    'test_case_completed':test_case_completed})

    def _notify(self,name,type,func,*args):
        for o in self._observer_list:
            o[func](name,type,*args)

    def _test_started_notify(self,name,type):
        self._notify(name,type,'test_started',time.asctime())

    def _test_stopped_notify(self,name,type):
        self._notify(name,type,'test_stopped',time.asctime())

    def _test_case_started(self,name,type,case):
        self._notify(name,type,'test_case_started',case)

    def _test_case_completed(self,name,type,case,result):
        self._notify(name,type,'test_case_completed',case,result)

    def _add_project_callback(self,name,type):
        if not self._test_cases.get(type,None):
            self._test_cases[type]={}

        if self._test_cases[type].get(name,None):
            self._test_cases[type][name]={'stime':None,'etime':None,'version':None,'thread':None,'stop_flag':False,'current_case':None,'case':{}}

    def _delete_project_callback(self,name,type):
        self.stop_test(name,type)

        try:
            self._test_cases[type].pop(name)
        except KeyError as e:
            pass

    def _modify_project_callback(self,name,type):
        pass

    def _test_run(self,project_type,project_name,project_dict,TM,TL):
        cases=TL.load_cases(project_type,project_name)
        for case in cases:
            if project_dict['stop_flag']:
                break
           
            TM._test_case_started(project_name,project_type,case.name())
            project_dict['case']=case.name()
            try:
                ret=case.run()
            except Exception as e:
                ret=False

            project_dict['cases'][case.name()]=ret
            TM._test_case_completed(project_name,project_type,case.name(),ret)

        project_dict['etime']=time.asctime()
        TM._test_stopped_notify(project_name,project_type)

    def test_running(self,project_type,project_name):
        try:
            thread=self._test_cases[project_type][project_name]['thread']
            if thread:
                return thread.isAlive()
            return False
        except KeyError as e:
            return False

    def start_test(self,project_type,project_name,version):
        if self.test_running(project_type,project_name):
            self.stop_test(project_type,project_name)

        if not self._test_cases.get(project_type,None):
            self._test_cases[project_type]={}

        if not self._test_case[project_type].get(project_name,None):
            self._test_cases[project_type][project_name]={'thread':None,
                        'stop_flag':False,
                        'stime':time.asctime(),
                        'etime':None,
                        'current_case':None,
                        'cases':{},
                        'version':version}
            t=threading.Thread(
                target=self._test_run,args=(project_type,project_name,
                        self._test_case[project_type][project_name],TL))
            self._test_case[project_type][project_name]['thread']=t
            t.start()
        else:
            self._test_case[project_type][project_name]['stop_flag']=False
            self._test_case[project_type][project_name]['thread']=
                threading.Thread(target=self._test_run,args=(project_type,project_name,
                        self._test_case[project_type][project_name],TL))
            self._test_case[project_type][project_name]['thread'].start()

        self._test_started_notify(project_name,project_type)

    def stop_test(self,project_type,project_name):
        if self.test_running(project_type,project_name):
            self._test_cases[project_type][project_name]['stop_flag']=True
            self._test_cases[project_type][project_name]['thread'].join()

        self._test_stopped_notify(project_name,project_type)

    def _get(self,project_name,project_type,key):
        try:
            return self._test_cases[project_type][project_name][key]
        except KeyError as e:
            return None

    def get_version(self,project_name,project_type):
        return self._get(project_name,project_type,'version')

    def get_current_test(self,project_name,project_type):
        return self._get(project_name,project_type,'current_case')

    def get_start_time(self,project_name,project_type):
        return self._get(project_name,project_type,'stime')

    def get_end_time(self,project_name,project_type):
        return self._get(project_name,project_type,'etime')

    def get_cases(self,project_name,project_type):
        return self._get(project_name,project_type,'cases')

TM=TestCaseManager()
