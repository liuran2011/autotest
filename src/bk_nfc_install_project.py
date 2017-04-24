from project import Project
from constants import *
from ConfigParser import ConfigParser
import os

class BKNFCInstallProject(Project):
    def __init__(self,name,type,**kwargs):
        super(BKNFCInstallProject,self).__init__(name,type)

        self.tenant=kwargs[NFC_INSTALL_PROJECT_TENANT]
        self.password=kwargs[NFC_INSTALL_PROJECT_PASSWORD]
        self.keystone_url=kwargs[NFC_INSTALL_PROJECT_KEYSTONE_URL]
        self.region=kwargs[NFC_INSTALL_PROJECT_REGION]
        self.public_network=kwargs[NFC_INSTALL_PROJECT_PUBLIC_NETWORK]
        self.cases=kwargs[NFC_INSTALL_PROJECT_CASES]

    @staticmethod
    def delete(project):
        os.remove(project.conf_file())
    
    @classmethod
    def load(cls,conf_file):
        conf=ConfigParser()
        conf.read(conf_file)
       
        name=os.path.basename(conf_file)
        type=NFC_INSTALL_TEST 
        tenant=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_TENANT)
        password=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PASSWORD)
        keystone_url=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_KEYSTONE_URL)
        region=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_REGION)
        public_network=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PUBLIC_NETWORK)
        cases=conf.get(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_CASES).split(',')
        
        return cls(name,type,tenant=tenant,password=password,keystone_url=keystone_url,
                    region=region,public_network=public_network,cases=cases)

    def modify(self,**kwargs):
        tenant=kwargs.get(NFC_INSTALL_PROJECT_TENANT,None)
        if tenant:
            self.tenant=tenant

        password=kwargs.get(NFC_INSTALL_PROJECT_PASSWORD,None)
        if password:
            self.password=password
        
        cases=kwargs.get(NFC_INSTALL_PROJECT_CASES,None)
        if cases:
            self.cases=cases
        
        self.save()

    def save(self):
        conf=ConfigParser()
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_NAME,self.name)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_TENANT,self.tenant)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PASSWORD,self.password)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_KEYSTONE_URL,self.keystone_url)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_REGION,self.region)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_PUBLIC_NETWORK,self.public_network)
        conf.set(CONF_DEFAULT_SECTION,NFC_INSTALL_PROJECT_CASES,",".join(self.cases))

        file=open(self.conf_file(),"w")
        conf.write(file) 
        file.close()
