from PyQt5.QtWidgets import QMainWindow
from giris_sayfasi_arayuz import Ui_MainWindow as giris_sayfasi_arayuz
from guvenlik_sorusu_arayuz import Ui_MainWindow as guvenlik_sorusu_arayuz
from sifre_ayarlar import Sifre_Ayarlari 
import sifreleme
import bildirimler
import dosya_islemleri

class Giris_Sayfasi(QMainWindow,giris_sayfasi_arayuz):
    def __init__(self):
        super().__init__()
        self.s_a = Sifre_Ayarlari()
        self.baglan_arayuz()
    def sifre_kontrol(self,girilen_sifre):
        return sifreleme.desifrele(girilen_sifre,"sifre_kaydi.txt")
    def kullanici_adi_kontrol(self,girilen_kullanici_adi):
        return sifreleme.desifrele(girilen_kullanici_adi,"kullanici_adi_kaydi.txt")
    
    def cevap_kontrol(self):
        girilen_cevap = self.ui_.cevap.text()
        if sifreleme.desifrele(girilen_cevap,"g_s_cevap.txt"):
            sifreleme.sifremi_ayarla("","sifre_kaydi.txt")
            self.pencere.close()
            self.s_a.show()
        else:
            bildirimler.mesaj_bildirim("HATALI GIRIS","Kullanici adi veya sifre girisi hatali.Lutfen tekrar deneyiniz!")
    def geri(self):
        self.pencere.close()
        self.show()
    def sifremi_unuttum(self):
        self.pencere = QMainWindow()
        self.ui_ = guvenlik_sorusu_arayuz()
        self.ui_.setupUi(self.pencere)
        self.pencere.show()
        self.ui_.guvenlik_sorusu.setText(dosya_islemleri.dosya_oku("guvenlik_sorusu.txt"))
        self.ui_.buton_geri.clicked.connect(self.geri)
        self.ui_.buton_devam.clicked.connect(self.cevap_kontrol)
    def baglan_arayuz(self):
        """
        Bu fonksiyonun gorevi Qt Designer'da olusturdugumuz arayuzu baglamaktir.
        """
        self.setupUi(self)
        self.baglantilar()
    def baglantilar(self):
        """
        Bu fonksiyonun gorevi arayuzdeki butonlari dinlemektir.
        Ve eger bu butonlardan birine tiklandiysa gerekli fonksiyona yonlendirir.
        """
        self.buton_sifremi_unuttum.clicked.connect(self.sifremi_unuttum)
