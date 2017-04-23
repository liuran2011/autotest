#coding=utf-8

import os

WORK_DIRECTORY="."
LOG_DIRECTORY=os.sep.join([WORK_DIRECTORY,"log"])
CONFIG_DIRECTORY=os.sep.join([WORK_DIRECTORY,"conf"])
PROJECTS_DIRECTORY=os.sep.join([WORK_DIRECTORY,"projects"])
TESTLOG_DIRECTORY=os.sep.join([PROJECTS_DIRECTORY,"logs"])
CONFIG_FILE=os.sep.join([CONFIG_DIRECTORY,"autotest.conf"])

CONF_DEFAULT_SECTION="DEFAULT"
CONF_NFC_INSTALL_TEST_SECTION="nfc_install_test"

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

CONF_NFC_INSTALL_TEST_SECTION_TEST_TYPES="test_types"

NFC_INSTALL_TEST_CTRL_HA="HA 总控+3主控+计算+TGW测试"
NFC_INSTALL_TEST_ALL_SEP="总控+主控+计算+TGW测试"
NFC_INSTALL_TEST_GLBCTRL="总主控+计算+TGW测试"
NFC_INSTALL_TEST_CTRLCOM="总控+主控计算+TGW测试"
CONF_NFC_INSTALL_TEST_SECTION_DEFAULT_TEST_TYPE_VALUE=",".join([NFC_INSTALL_TEST_CTRL_HA,
                                                                NFC_INSTALL_TEST_ALL_SEP,
                                                                NFC_INSTALL_TEST_GLBCTRL,
                                                                NFC_INSTALL_TEST_CTRLCOM])
