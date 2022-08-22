from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 675)
        MainWindow.setMinimumSize(QtCore.QSize(967, 675))
        MainWindow.setMaximumSize(QtCore.QSize(967, 675))
        MainWindow.setStyleSheet("color:rgb(139 ,26 ,26);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.312, y1:0.710045, x2:0.927, y2:0.165, stop:0.265537 rgba(255, 235, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buton_calisma = QtWidgets.QPushButton(self.centralwidget)
        self.buton_calisma.setMinimumSize(QtCore.QSize(300, 70))
        self.buton_calisma.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buton_calisma.setFont(font)
        self.buton_calisma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_calisma.setStyleSheet("font: 20pt \"Palatino Linotype\";\n"
"color:rgb(139 ,26 ,26);\n"
"border-style: outset;\n"
"border-color:rgb(139 ,26 ,26);\n"
"border-width:2px;")
        self.buton_calisma.setObjectName("buton_calisma")
        self.verticalLayout.addWidget(self.buton_calisma)
        self.buton_notlar = QtWidgets.QPushButton(self.centralwidget)
        self.buton_notlar.setMinimumSize(QtCore.QSize(200, 70))
        self.buton_notlar.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buton_notlar.setFont(font)
        self.buton_notlar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_notlar.setStyleSheet("font: 22pt \"Palatino Linotype\";\n"
"color:rgb(139 ,26 ,26);\n"
"border-style: outset;\n"
"border-color:rgb(139 ,26 ,26);\n"
"border-width:2px;")
        self.buton_notlar.setObjectName("buton_notlar")
        self.verticalLayout.addWidget(self.buton_notlar)
        self.buton_rapor = QtWidgets.QPushButton(self.centralwidget)
        self.buton_rapor.setMinimumSize(QtCore.QSize(300, 70))
        self.buton_rapor.setMaximumSize(QtCore.QSize(300, 70))
        self.buton_rapor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_rapor.setStyleSheet("font: 22pt \"Palatino Linotype\";\n"
"color:rgb(139 ,26 ,26);\n"
"border-style: outset;\n"
"border-color:rgb(139 ,26 ,26);\n"
"border-width:2px;")
        self.buton_rapor.setObjectName("buton_rapor")
        self.verticalLayout.addWidget(self.buton_rapor)
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_geri.setMinimumSize(QtCore.QSize(300, 70))
        self.buton_geri.setMaximumSize(QtCore.QSize(300, 70))
        self.buton_geri.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_geri.setStyleSheet("font: 22pt \"Palatino Linotype\";\n"
"color:rgb(139 ,26 ,26);\n"
"border-style: outset;\n"
"border-color:rgb(139 ,26 ,26);\n"
"border-width:2px;")
        self.buton_geri.setObjectName("buton_geri")
        self.verticalLayout.addWidget(self.buton_geri)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 23))
        self.menubar.setObjectName("menubar")
        self.yardim = QtWidgets.QMenu(self.menubar)
        self.yardim.setObjectName("yardim")
        self.ayarlar = QtWidgets.QMenu(self.yardim)
        self.ayarlar.setObjectName("ayarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hakkimizda = QtWidgets.QAction(MainWindow)
        self.hakkimizda.setObjectName("hakkimizda")
        self.nasilKullanilir = QtWidgets.QAction(MainWindow)
        self.nasilKullanilir.setObjectName("nasilKullanilir")
        self.sifre_ayarlar = QtWidgets.QAction(MainWindow)
        self.sifre_ayarlar.setObjectName("sifre_ayarlar")
        self.bildirim_Ayarlar = QtWidgets.QAction(MainWindow)
        self.bildirim_Ayarlar.setObjectName("bildirim_Ayarlar")
        self.actionG_venlik_Ayarlari = QtWidgets.QAction(MainWindow)
        self.actionG_venlik_Ayarlari.setObjectName("actionG_venlik_Ayarlari")
        self.action_k_Yap = QtWidgets.QAction(MainWindow)
        self.action_k_Yap.setObjectName("action_k_Yap")
        self.ayarlar.addAction(self.sifre_ayarlar)
        self.ayarlar.addAction(self.bildirim_Ayarlar)
        self.ayarlar.addAction(self.actionG_venlik_Ayarlari)
        self.yardim.addAction(self.ayarlar.menuAction())
        self.yardim.addAction(self.hakkimizda)
        self.menubar.addAction(self.yardim.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AJANDAM"))
        self.buton_calisma.setText(_translate("MainWindow", "CALISMA"))
        self.buton_notlar.setText(_translate("MainWindow", "NOTLAR"))
        self.buton_rapor.setText(_translate("MainWindow", "Haftalik Rapor"))
        self.buton_geri.setText(_translate("MainWindow", "GERI"))
        self.yardim.setTitle(_translate("MainWindow", "Yardim"))
        self.ayarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.hakkimizda.setText(_translate("MainWindow", "Hakkimizda"))
        self.nasilKullanilir.setText(_translate("MainWindow", "Nasil Kullanilir?"))
        self.sifre_ayarlar.setText(_translate("MainWindow", "Sifre Ayarlari"))
        self.bildirim_Ayarlar.setText(_translate("MainWindow", "Bildirim Ayarlari"))
        self.actionG_venlik_Ayarlari.setText(_translate("MainWindow", "Guvenlik Ayarlari"))
        self.action_k_Yap.setText(_translate("MainWindow", "Cikis Yap"))

