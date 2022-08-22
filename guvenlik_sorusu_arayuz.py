#Bu dosya "Qt Designer" 'da tasarladigimiz arayuzlerin .py uzantili dosyasidir.
#Arayuzleri donustururken "design2pyconverter" uygulamasini kullandik.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 165)
        MainWindow.setMinimumSize(QtCore.QSize(395, 165))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 165))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_geri.setMinimumSize(QtCore.QSize(80, 0))
        self.buton_geri.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_geri.setFont(font)
        self.buton_geri.setObjectName("buton_geri")
        self.gridLayout.addWidget(self.buton_geri, 6, 0, 1, 1)
        self.guvenlik_sorusu = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.guvenlik_sorusu.setFont(font)
        self.guvenlik_sorusu.setObjectName("guvenlik_sorusu")
        self.gridLayout.addWidget(self.guvenlik_sorusu, 0, 0, 1, 3)
        self.cevap = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cevap.setFont(font)
        self.cevap.setObjectName("cevap")
        self.gridLayout.addWidget(self.cevap, 2, 0, 1, 1)
        self.buton_devam = QtWidgets.QPushButton(self.centralwidget)
        self.buton_devam.setMinimumSize(QtCore.QSize(100, 0))
        self.buton_devam.setMaximumSize(QtCore.QSize(60, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_devam.setFont(font)
        self.buton_devam.setObjectName("buton_devam")
        self.gridLayout.addWidget(self.buton_devam, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ajanda"))
        self.buton_geri.setText(_translate("MainWindow", "GERI"))
        self.guvenlik_sorusu.setText(_translate("MainWindow", "TextLabel"))
        self.buton_devam.setText(_translate("MainWindow", "DEVAM"))

