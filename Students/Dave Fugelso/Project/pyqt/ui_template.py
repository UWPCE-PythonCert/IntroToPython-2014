# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template1.ui'
#
# Created: Thu Dec 11 21:43:48 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Template1(object):
    def setupUi(self, Template1):
        Template1.setObjectName(_fromUtf8("Template1"))
        Template1.resize(500, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Template1.sizePolicy().hasHeightForWidth())
        Template1.setSizePolicy(sizePolicy)
        self.btn01 = QtGui.QToolButton(Template1)
        self.btn01.setGeometry(QtCore.QRect(17, 223, 76, 60))
        self.btn01.setObjectName(_fromUtf8("btn01"))
        self.btn02 = QtGui.QToolButton(Template1)
        self.btn02.setGeometry(QtCore.QRect(95, 223, 76, 60))
        self.btn02.setObjectName(_fromUtf8("btn02"))
        self.btn03 = QtGui.QToolButton(Template1)
        self.btn03.setGeometry(QtCore.QRect(173, 223, 76, 60))
        self.btn03.setObjectName(_fromUtf8("btn03"))
        self.btn04 = QtGui.QToolButton(Template1)
        self.btn04.setGeometry(QtCore.QRect(251, 223, 76, 60))
        self.btn04.setObjectName(_fromUtf8("btn04"))
        self.btn05 = QtGui.QToolButton(Template1)
        self.btn05.setGeometry(QtCore.QRect(329, 223, 76, 60))
        self.btn05.setObjectName(_fromUtf8("btn05"))
        self.btn06 = QtGui.QToolButton(Template1)
        self.btn06.setGeometry(QtCore.QRect(407, 223, 76, 60))
        self.btn06.setObjectName(_fromUtf8("btn06"))
        self.img01 = QtGui.QLabel(Template1)
        self.img01.setGeometry(QtCore.QRect(16, 84, 100, 100))
        self.img01.setObjectName(_fromUtf8("img01"))
        self.img02 = QtGui.QLabel(Template1)
        self.img02.setGeometry(QtCore.QRect(463, 70, 25, 25))
        self.img02.setObjectName(_fromUtf8("img02"))
        self.imgtitle = QtGui.QLabel(Template1)
        self.imgtitle.setGeometry(QtCore.QRect(0, 0, 250, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Saab"))
        font.setPointSize(25)
        self.imgtitle.setFont(font)
        self.imgtitle.setAutoFillBackground(True)
        self.imgtitle.setObjectName(_fromUtf8("imgtitle"))
        self.text01 = QtGui.QLineEdit(Template1)
        self.text01.setGeometry(QtCore.QRect(128, 84, 310, 22))
        self.text01.setObjectName(_fromUtf8("text01"))
        self.text02 = QtGui.QLineEdit(Template1)
        self.text02.setGeometry(QtCore.QRect(128, 112, 310, 24))
        self.text02.setObjectName(_fromUtf8("text02"))
        self.text03 = QtGui.QLineEdit(Template1)
        self.text03.setGeometry(QtCore.QRect(128, 146, 310, 22))
        self.text03.setObjectName(_fromUtf8("text03"))
        self.text04 = QtGui.QLineEdit(Template1)
        self.text04.setGeometry(QtCore.QRect(406, 194, 72, 18))
        self.text04.setObjectName(_fromUtf8("text04"))
        self.progbar = QtGui.QProgressBar(Template1)
        self.progbar.setGeometry(QtCore.QRect(128, 197, 270, 14))
        self.progbar.setProperty("value", 24)
        self.progbar.setObjectName(_fromUtf8("progbar"))
        self.sbar = QtGui.QLabel(Template1)
        self.sbar.setGeometry(QtCore.QRect(250, 0, 250, 45))
        self.sbar.setText(_fromUtf8(""))
        self.sbar.setObjectName(_fromUtf8("sbar"))

        self.retranslateUi(Template1)
        QtCore.QMetaObject.connectSlotsByName(Template1)

    def retranslateUi(self, Template1):
        Template1.setWindowTitle(_translate("Template1", "Dialog", None))
        self.btn01.setText(_translate("Template1", "...", None))
        self.btn02.setText(_translate("Template1", "...", None))
        self.btn03.setText(_translate("Template1", "...", None))
        self.btn04.setText(_translate("Template1", "...", None))
        self.btn05.setText(_translate("Template1", "...", None))
        self.btn06.setText(_translate("Template1", "...", None))
        self.img01.setText(_translate("Template1", "TextLabel", None))
        self.img02.setText(_translate("Template1", "TextLabel", None))
        self.imgtitle.setText(_translate("Template1", "TextLabel", None))

