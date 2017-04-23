from project import Project
from constants import *
from ConfigParser import ConfigParser

class BKNFCInstallProject(Project):
    def __init__(self,name,type,**kwargs):
        super(BKNFCInstallProject,self).__init__(name,type)

        self.tenant=kwargs[NFC_INSTALL_PROJECT_TENANT]
        self.password=kwargs[NFC_INSTALL_PROJECT_PASSWORD]
        self.keystone_url=kwargs[NFC_INSTALL_PROJECT_KEYSTONE_URL]
        self.region=kwargs[NFC_INSTALL_PROJECT_REGION]
        self.public_network=kwargs[NFC_INSTALL_PROJECT_PUBLIC_NETWORK]
    
    def save(self):
        conf=ConfigParser()
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_NAME,self.name)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_TENANT,self.tenant)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PASSWORD,self.password)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_KEYSTONE_URL,self.keystone_url)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_REGION,self.region)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PUBLIC_NETWORK,self.public_network)

        file=open(self.conf_file(),"w")
        conf.write(file) 
        file.close()
