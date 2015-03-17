# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forme.ui'
#
# Created: Thu Feb  5 22:21:09 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import sys
import time
from kit3 import get_list_contest
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import QtCore, QtGui


fcnt,pcnt=get_list_contest()    #from previous files...............:D

stringfc=str()
stringpc=str()

    
        






try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(630, 424)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 10pt \"Comic Sans MS\";\n"
"border-color: rgb(255, 0, 0);\n"
"background-color: rgb(146, 166, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(146, 166, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"font: 75 10pt \"Comic Sans MS\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 219, 252);\n"
"border-color: rgb(85, 0, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.present_contests)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.future_contests)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "kitchen status", None))
        self.pushButton_2.setText(_translate("Form", "upcoming recipes", None))
        self.label.setText(_translate("Form", "click to see the kitchen status", None))

    def present_contests(self) :
        self.label.setText(stringpc)

    def future_contests(self) :
        self.label.setText(stringfc)





for i in fcnt :
    stringfc=stringfc +  '            '+  i[0]+'        '+i[1]+'        '+time.strftime('%Y-%m-%d %H:%M:%S',i[2])+'        '+time.strftime('%Y-%m-%d %H:%M:%S',i[3])+"\n"
    
for i in pcnt :
    stringpc=stringpc +  '            '+i[0]+'        '+i[1]+'        '+time.strftime('%Y-%m-%d %H:%M:%S',i[2])+'        '+time.strftime('%Y-%m-%d %H:%M:%S',i[3])+"\n" 




app =QtGui.QApplication(sys.argv)
Form=QtGui.QWidget()
ui=Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
    
    

        

