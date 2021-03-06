from ConfigParser import ConfigParser
from env import ENV
import os
from constants import *

class Config(object):
    def __init__(self):
        self.conf=ConfigParser()

        if os.path.exists(ENV.conf_file()):
            self._load_config()
        else:
            self._gen_default_config()

    def _load_config(self):
        self.conf.read(ENV.conf_file())
 
    def _gen_default_config(self):
        self.conf.set(CONF_DEFAULT_SECTION,
                    CONF_DEFAULT_SECTION_DEFAULT_PROJECT_TYPE,
                    CONF_DEFAULT_SECTION_DEFAULT_PROJECT_TYPE_VALUE)

        self.conf.add_section(CONF_NFC_INSTALL_TEST_SECTION)
        self.conf.set(CONF_NFC_INSTALL_TEST_SECTION,
                      CONF_NFC_INSTALL_TEST_SECTION_TEST_TYPES,
                      CONF_NFC_INSTALL_TEST_SECTION_DEFAULT_TEST_TYPE_VALUE)
        f=open(ENV.conf_file(),"w")
        self.conf.write(f)
        f.close()

    def project_type_list(self):
        types=self.conf.get(CONF_DEFAULT_SECTION,CONF_DEFAULT_SECTION_DEFAULT_PROJECT_TYPE)
        return types.split(',')

    def nfc_test_list(self):
        types=self.conf.get(CONF_NFC_INSTALL_TEST_SECTION,CONF_NFC_INSTALL_TEST_SECTION_TEST_TYPES)
        return types.split(',')

CONF=Config()
