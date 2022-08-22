#Bu dosya "Qt Designer" 'da tasarladigimiz arayuzlerin .py uzantili dosyasidir.
#Arayuzleri donustururken "design2pyconverter" uygulamasini kullandik.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 219)
        MainWindow.setMinimumSize(QtCore.QSize(451, 219))
        MainWindow.setMaximumSize(QtCore.QSize(451, 16777215))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.08, y1:0.108, x2:1, y2:1, stop:0.363184 rgba(73, 111, 139, 152), stop:0.711443 rgba(103, 158, 197, 255), stop:1 rgba(239, 242, 241, 152));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 416, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_geri = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_geri.setMinimumSize(QtCore.QSize(100, 50))
        self.buton_geri.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buton_geri.setFont(font)
        self.buton_geri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_geri.setStyleSheet("color:white;\n"
"font: 14pt \"NSimSun\";\n"
"border-style: outset;\n"
"border-color: white;\n"
"border-width:2px;")
        self.buton_geri.setObjectName("buton_geri")
        self.horizontalLayout.addWidget(self.buton_geri)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buton_kaydet = QtWidgets.QPushButton(self.layoutWidget)
        self.buton_kaydet.setMinimumSize(QtCore.QSize(250, 50))
        self.buton_kaydet.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buton_kaydet.setFont(font)
        self.buton_kaydet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_kaydet.setStyleSheet("color:white;\n"
"font: 14pt \"NSimSun\";\n"
"border-style: outset;\n"
"border-color: white;\n"
"border-width:2px;")
        self.buton_kaydet.setObjectName("buton_kaydet")
        self.horizontalLayout.addWidget(self.buton_kaydet)
        self.comboBox_bildirim = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_bildirim.setGeometry(QtCore.QRect(40, 40, 381, 61))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_bildirim.setFont(font)
        self.comboBox_bildirim.setStyleSheet("\n"
"font: 14pt \"NSimSun\";")
        self.comboBox_bildirim.setObjectName("comboBox_bildirim")
        self.comboBox_bildirim.addItem("")
        self.comboBox_bildirim.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buton_geri.setText(_translate("MainWindow", "GERI"))
        self.buton_kaydet.setText(_translate("MainWindow", "Degisiklikleri Kaydet"))
        self.comboBox_bildirim.setItemText(0, _translate("MainWindow", "Sesle Bildirim Almak Istiyorum"))
        self.comboBox_bildirim.setItemText(1, _translate("MainWindow", "Pencereyle Bildirim Almak Istiyorum"))

