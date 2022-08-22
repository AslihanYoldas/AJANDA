from PyQt5.QtWidgets import QMainWindow,QMessageBox
import bildirimler as bildir
import sifreleme
from sifre_ayarlar_arayuz import Ui_MainWindow as sifre_ayar
class Sifre_Ayarlari(QMainWindow):
    """Sifre ayari arayuzunu olusturdugumuz ve kayit yapma ,sifre degistirme islemlerini saglayan sifre ayari sinifi"""
    def __init__(self):
        super(Sifre_Ayarlari,self).__init__()
        self.basla()
    def basla(self):
        """Arayuzu olusturuyoruz,butonu etkinlestiriyoruz"""
        self.ui = sifre_ayar()
        self.ui.setupUi(self)
        self.baglantilar()
    def closeEvent(self, event):
        """'X' basilmissa yani sekme kapatilmak istenmis ise Kapatmak istediginize emin misiniz diye sorar
         Yes'e basilirsa kapatilir No'ya basilirsa kapanmaz"""
        kapat = QMessageBox.question(self,
                                     "CIKIS",
                                     "Kapatmak istediginize emin misiniz?",
                                      QMessageBox.Yes | QMessageBox.No)
        if kapat == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def sifre_degistir(self):
        """Kullanici kayit olurken, sifre degistirirken bu fonksiyonu cagriyoruz. Kayit oluyorsa kullanici adini
        ve sifresini dosyalara sifreleyerek yaziyoruz. Sifresini degistiriyorsa kullanici adini ve mevcut sifresini
        dosyadan desifreleyerek okuyoruz kullanicinin girdigi kullanici adi ve eski sifre ile uyusuyorsa girdigi yeni
        sifreyi dosyaya kaydediyoruz. Boylece sifresini degistirmis oluyor
        """
        kullanici_adi=self.ui.lineEdit_kullaniciAdi.text()
        eski_sifre=self.ui.lineEdit_EskiSifre.text()
        yeni_sifre=self.ui.lineEdit_YeniSifre.text()
        #Kayit
        if sifreleme.desifrele("", "kullanici_adi_kaydi.txt") and sifreleme.desifrele("", "sifre_kaydi.txt") :
            sifreleme.sifremi_ayarla(yeni_sifre, "sifre_kaydi.txt")
            sifreleme.sifremi_ayarla(kullanici_adi, "kullanici_adi_kaydi.txt")
            bildir.mesaj_bildirim("Bilgilendirme","Kayıt yapıldı")
            self.close()
        #Sifre degistirme
        elif sifreleme.desifrele(kullanici_adi, "kullanici_adi_kaydi.txt") and sifreleme.desifrele(eski_sifre, "sifre_kaydi.txt") :
            sifreleme.sifremi_ayarla(yeni_sifre, "sifre_kaydi.txt")
            bildir.mesaj_bildirim("Bilgilendirme","Yeni sifre basariyla ayarlandi")
        else:
            bildir.mesaj_bildirim("Sifre degistirilemedi", "Kullanici adi veya sifre yanlis tekrar deneyin")

    def baglantilar(self):
        """
        Bu fonksiyonun gorevi arayuzdeki butonlari dinlemektir.
        Ve eger bu butonlardan birine tiklandiysa gerekli fonksiyona yonlendirir.
        sifre_degistir butonuna basinca sifre_degistir fonksiyonuna yonlendiriyor
        """
        self.ui.buton_sifre_degistir.clicked.connect(self.sifre_degistir)
            
        


