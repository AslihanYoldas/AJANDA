from PyQt5.QtWidgets import QMainWindow,QMessageBox
import bildirimler as bildir
import sifreleme
from guvenlik_ayarlari_arayuz import Ui_MainWindow as guv_ayar
class Guvenlik_Ayarlari(QMainWindow):
    def __init__(self):
        super(Guvenlik_Ayarlari,self).__init__()
        self.basla()
    def basla(self):
        self.ui = guv_ayar()#arayüzdeki sınıftan bir nesne oluşturuyoruz
        self.ui.setupUi(self)
        self.baglantilar()
    def guvenlik_sorusu(self):
        guvenlik_cevap=self.ui.lineEdit_guvenlik_cevap.text()
        sifreleme.sifremi_ayarla(guvenlik_cevap,"g_s_cevap.txt")
        bildir.mesaj_bildirim("Bilgilendirme","Guvenlik sorusunun cevabi kaydedildi")
    def closeEvent(self, event):
        """'X' basılmışsa yani sekme kapatılmak istenmiş ise Kapatmak istediğinize emin misiniz diye sorar
         Yes'e basılrsa kapatılır no ya basılırsa kapanmaz"""
        kapat = QMessageBox.question(self,
                                     "ÇIKIŞ",
                                     "Kapatmak istediginize emin misiniz?",
                                      QMessageBox.Yes | QMessageBox.No)
        if kapat == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def baglantilar(self):
        """
        Bu fonksiyonun gorevi arayuzdeki butonlari dinlemektir.
        Ve eger bu butonlardan birine tiklandiysa gerekli fonksiyona yonlendirir.
        """
        self.ui.buton_kaydet_degistir.clicked.connect(self.guvenlik_sorusu)
