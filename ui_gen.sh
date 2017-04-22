#!/bin/sh

./pyuic5 mainwindow.ui -o src/ui_mainwindow.py
./pyuic5 new_project_select.ui -o src/ui_new_project_select.py
./pyuic5 delete_project.ui -o src/ui_delete_project.py
./pyuic5 nfc_install_project.ui -o src/ui_nfc_install_project.py
./pyuic5 setting_project.ui -o src/ui_setting_project.py
./pyuic5 nfc_setting.ui -o src/ui_nfc_setting.py
./pyuic5 project_types.ui -o src/ui_project_types.py
./pyuic5 about.ui -o src/ui_about.py
