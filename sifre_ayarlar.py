from PyQt5.QtWidgets import QMainWindow,QMessageBox
import bildirimler as bildir
import sifreleme
from sifre_ayarlar_arayuz import Ui_MainWindow as sifre_ayar
class Sifre_Ayarlari(QMainWindow):
    def __init__(self):
        super(Sifre_Ayarlari,self).__init__()
        self.basla()
    def basla(self):
        self.ui = sifre_ayar()#arayüzdeki sınıftan bir nesne oluşturuyoruz
        self.ui.setupUi(self)
        self.baglantilar()
    def closeEvent(self, event):
        """'X' basılmışsa yani sekme kapatılmak istenmiş ise Kapatmak istediğinize emin misiniz diye sorar
         Yes'e basılrsa kapatılır no ya basılırsa kapanmaz"""
        kapat = QMessageBox.question(self,
                                     "CIKIS",
                                     "Kapatmak istediginize emin misiniz?",
                                      QMessageBox.Yes | QMessageBox.No)
        if kapat == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def sifre_degistir(self):
        kullanici_adi=self.ui.lineEdit_kullaniciAdi.text()
        eski_sifre=self.ui.lineEdit_EskiSifre.text()
        yeni_sifre=self.ui.lineEdit_YeniSifre.text()
        if sifreleme.desifrele(kullanici_adi, "kullanici_adi_kaydi.txt") and sifreleme.desifrele(eski_sifre, "sifre_kaydi.txt") :
            sifreleme.sifremi_ayarla(yeni_sifre, "sifre_kaydi.txt")
            bildir.mesaj_bildirim("Bilgilendirme","Yeni sifre basariyla ayarlandi")
        else:
            bildir.mesaj_bildirim("Sifre degistirilemedi", "Kullanici adi veya sifre yanlis tekrar deneyin")
    def baglantilar(self):
        """
        Bu fonksiyonun gorevi arayuzdeki butonlari dinlemektir.
        Ve eger bu butonlardan birine tiklandiysa gerekli fonksiyona yonlendirir.
        """
        self.ui.buton_sifre_degistir.clicked.connect(self.sifre_degistir)
            
        


