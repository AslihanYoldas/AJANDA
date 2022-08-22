# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/UET_URAN_010/Desktop/notlar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 537)
        MainWindow.setMinimumSize(QtCore.QSize(550, 537))
        MainWindow.setMaximumSize(QtCore.QSize(550, 537))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 27pt  \"NSimSun\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.notlar = QtWidgets.QTextEdit(self.centralwidget)
        self.notlar.setMinimumSize(QtCore.QSize(500, 0))
        self.notlar.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.notlar.setFont(font)
        self.notlar.setStyleSheet("font: 16pt \"Arial Narrow\";")
        self.notlar.setFrameShape(QtWidgets.QFrame.Box)
        self.notlar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.notlar.setObjectName("notlar")
        self.verticalLayout.addWidget(self.notlar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AJANDAM"))
        self.label.setText(_translate("MainWindow", "NOTLAR"))
        self.notlar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Narrow\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:15pt;\"><br /></p></body></html>"))

