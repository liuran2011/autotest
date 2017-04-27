from env import ENV
import time
import os

class TestLog(object):
    def __init__(self,project_type,project_name):
        self._test_log_file_name=self._test_log_file(project_type,project_name)
        self._file=open(self._test_log_file_name,"w")

    def _test_log_file(self,project_type,project_name):
        test_log_dir=ENV.test_log_directory(project_type)
        return os.path.join(test_log_dir,"%s-%s.log"%(project_name,time.strftime("%Y%m%d%H%M%S")))

    def close(self):
        if self._file:
            self._file.close()

    def _write(self,level,log):
        self._file.write("[%s][%s]%s\n"%(level,time.asctime(),log))

    def info(self,log):
        self._write('info',log)

    def warn(self,log):
        self._write('warn',log)

    def error(self,log):
        self._write('error',log)

    def debug(self,log):
        self._write('debug',log)
