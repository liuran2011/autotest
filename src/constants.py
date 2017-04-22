#coding=utf-8

import os

WORK_DIRECTORY="."
LOG_DIRECTORY=os.sep.join([WORK_DIRECTORY,"log"])
CONFIG_DIRECTORY=os.sep.join([WORK_DIRECTORY,"conf"])
PROJECTS_DIRECTORY=os.sep.join([WORK_DIRECTORY,"projects"])
TESTLOG_DIRECTORY=os.sep.join([PROJECTS_DIRECTORY,"logs"])
CONFIG_FILE=os.sep.join([CONFIG_DIRECTORY,"autotest.conf"])

CONF_DEFAULT_SECTION="DEFAULT"
CONF_DEFAULT_SECTION_DEFAULT_PROJECT_TYPE="project_types"

NFC_INSTALL_TEST="NFC安装测试"
NFC_AUTO_TEST="NFC自动化测试"
CENI_INSTALL_TEST="CENI安装测试"
CENI_AUTO_TEST="CENI自动化测试"
SWITCH_AUTO_TEST="交换机自动化测试"
CONF_DEFAULT_SECTION_DEFAULT_PROJECT_TYPE_VALUE=",".join([NFC_INSTALL_TEST,
                                                          NFC_AUTO_TEST,
                                                          CENI_INSTALL_TEST,
                                                          CENI_AUTO_TEST,
                                                          SWITCH_AUTO_TEST])

