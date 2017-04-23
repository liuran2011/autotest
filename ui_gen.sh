#!/bin/sh

./pyuic5 mainwindow.ui -o src/ui_mainwindow.py
./pyuic5 new_project_select.ui -o src/ui_new_project_select.py
./pyuic5 delete_project.ui -o src/ui_delete_project.py
./pyuic5 nfc_install_project.ui -o src/ui_nfc_install_project.py
./pyuic5 setting_project.ui -o src/ui_setting_project.py
./pyuic5 nfc_setting.ui -o src/ui_nfc_setting.py
./pyuic5 nfc_project_main.ui -o src/ui_nfc_project_main.py
./pyuic5 nfc_auto_test_main.ui -o src/ui_nfc_auto_test_main.py
./pyuic5 ceni_install_main.ui -o src/ui_ceni_install_main.py
./pyuic5 ceni_auto_test_main.ui -o src/ui_ceni_auto_test_main.py
./pyuic5 switch_auto_test_main.ui -o src/ui_switch_auto_test_main.py
./pyuic5 nfc_test_types.ui -o src/ui_nfc_test_types.py
./pyuic5 about.ui -o src/ui_about.py
