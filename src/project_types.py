from ui_project_types import Ui_projectTypes
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget
from config import CONF

class ProjectTypes(QWidget,Ui_projectTypes):
    def __init__(self,parent=None):
        super(ProjectTypes,self).__init__(parent)

        self.setupUi(self)
        self._setup_radio_btn()
        self._retranslate_radio_btn()

    def _setup_radio_btn(self):
        self.radio_btns_dict={}
        types=CONF.project_type_list()
        for type in types:
            print type
            btn=QtWidgets.QRadioButton(self.groupBox)
            btn.setObjectName(type)
            self.radio_btns_dict[type]=btn

    def _retranslate_radio_btn(self):
        _trans=QtCore.QCoreApplication.translate
        for type in self.radio_btns_dict:
            self.radio_btns_dict[type].setText(_trans("projectTypes",type))
