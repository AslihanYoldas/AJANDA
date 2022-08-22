from PyQt5.QtWidgets import QMainWindow,QMessageBox
import bildirimler as bildir
import sifreleme
from guvenlik_ayarlari_arayuz import Ui_MainWindow as guv_ayar
class Guvenlik_Ayarlari(QMainWindow):
    """Guvenlik ayari arayuzunu olusturdugumuz ve verilen guvenlik sorusuna kullanicinin
    girdigi cevabi sifreli bir sekilde kaydeden guvenlik ayari sinifi"""
    def __init__(self):
        super(Guvenlik_Ayarlari,self).__init__()
        self.basla()
    def basla(self):
        """Arayuzu olusturuyoruz,butonu etkinlestiriyoruz"""
        self.ui = guv_ayar()
        self.ui.setupUi(self)
        self.baglantilar()
    def guvenlik_sorusu(self):
        """Kullanicinin girdigi cevabi sonradan sifremi unuttum secenegi icin 
        kullanilmak uzere txt dosyasına sifreleyerek yaziyoruz
        """
        guvenlik_cevap=self.ui.lineEdit_guvenlik_cevap.text()
        sifreleme.sifremi_ayarla(guvenlik_cevap,"g_s_cevap.txt")
        bildir.mesaj_bildirim("Bilgilendirme","Guvenlik sorusunun cevabi kaydedildi")
    def closeEvent(self, event):
        """'X' basilmissa yani sekme kapatilmak istenmis ise Kapatmak istediginize emin misiniz diye sorar
         Yes'e basilirsa kapatilir No'ya basilirsa kapanmaz"""
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
        kaydet butonuna basinca guvenlik_sorusu fonksiyonuna yonlendiriyor
        """
        self.ui.buton_kaydet_degistir.clicked.connect(self.guvenlik_sorusu)
