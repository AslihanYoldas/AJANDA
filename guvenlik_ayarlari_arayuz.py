#Bu dosya "Qt Designer" 'da tasarladigimiz arayuzlerin .py uzantili dosyasidir.
#Arayuzleri donustururken "design2pyconverter" uygulamasini kullandik.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 219)
        MainWindow.setMinimumSize(QtCore.QSize(451, 219))
        MainWindow.setMaximumSize(QtCore.QSize(451, 219))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.08, y1:0.108, x2:1, y2:1, stop:0.363184 rgba(73, 111, 139, 152), stop:0.711443 rgba(103, 158, 197, 255), stop:1 rgba(239, 242, 241, 152));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_guvenlik_sorusu = QtWidgets.QLabel(self.centralwidget)
        self.label_guvenlik_sorusu.setStyleSheet("font: 18pt \"NSimSun\";\n"
"color: rgb(255, 255, 255);")
        self.label_guvenlik_sorusu.setObjectName("label_guvenlik_sorusu")
        self.verticalLayout.addWidget(self.label_guvenlik_sorusu)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.lineEdit_guvenlik_cevap = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_guvenlik_cevap.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_guvenlik_cevap.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_guvenlik_cevap.setFont(font)
        self.lineEdit_guvenlik_cevap.setToolTip("")
        self.lineEdit_guvenlik_cevap.setStyleSheet("font: 14pt \"NSimSun\";")
        self.lineEdit_guvenlik_cevap.setText("")
        self.lineEdit_guvenlik_cevap.setFrame(False)
        self.lineEdit_guvenlik_cevap.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_guvenlik_cevap.setClearButtonEnabled(True)
        self.lineEdit_guvenlik_cevap.setObjectName("lineEdit_guvenlik_cevap")
        self.gridLayout.addWidget(self.lineEdit_guvenlik_cevap, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.buton_kaydet_degistir = QtWidgets.QPushButton(self.centralwidget)
        self.buton_kaydet_degistir.setMinimumSize(QtCore.QSize(200, 50))
        self.buton_kaydet_degistir.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buton_kaydet_degistir.setFont(font)
        self.buton_kaydet_degistir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_kaydet_degistir.setStyleSheet("color:white;\n"
"font: 14pt \"NSimSun\";\n"
"border-style: outset;\n"
"border-color: white;\n"
"border-width:2px;")
        self.buton_kaydet_degistir.setObjectName("buton_kaydet_degistir")
        self.horizontalLayout.addWidget(self.buton_kaydet_degistir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_guvenlik_sorusu.setText(_translate("MainWindow", "Ilkokul Ogretmeninizin adi nedir?"))
        self.buton_geri.setText(_translate("MainWindow", "GERI"))
        self.buton_kaydet_degistir.setText(_translate("MainWindow", "KAYDET/DEGISIKLIKLERİ KAYDET"))

