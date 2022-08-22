from giris_sayfasi import Giris_Sayfasi
from ana_sayfa_arayuz import Ui_MainWindow as Ana_Sayfa
from rapor import Rapor
from Notlar import Notlar
from sifre_ayarlar import Sifre_Ayarlari 
from bildirim_ayarlari import Bildirim_Ayarlari
from guvenlik_ayarlari import Guvenlik_Ayarlari
from hakkimizda_arayuz import Ui_MainWindow as Hakkimizda
from PyQt5.QtWidgets import QApplication,QMainWindow
import bildirimler
from calisma_sayfasi import Calisma_sayfasi
import dosya_islemleri as d_i
import tahmin


def hesap_giris():
    girilen_kullanici_adi = giris_s.girilen_kullanici_adi.text()
    girilen_sifre = giris_s.girilen_sifre.text()
    if giris_s.sifre_kontrol(girilen_sifre) and giris_s.kullanici_adi_kontrol(girilen_kullanici_adi):
        giris_s.close()
        ana_sayfa()
    else:
        bildirimler.mesaj_bildirim("HATALI GIRIS","Kullanici adi veya sifre girisi hatali.Lutfen tekrar deneyiniz!")
    
def giris():
    giris_s.show()
    giris_s.buton_giris.clicked.connect(hesap_giris)
def geri_giris():
    ana_pencere.close()
    giris_s.show()
def notlar():
    not_s.notlar.setText(d_i.dosya_oku("notlar.txt"))
    not_s.show()
def sifre_ayarlar_gir():
    s_a.show()
def bildirim_ayarlar_gir():
    b_a.show()
def guvenlik_ayarlar_gir():
    g_a.show()
        
def geri_ana_sayfa():
    calisma_s.close()
    ana_pencere.show()
    
def hakkimizda():
    hakkimizda_pencere.show()
    
def rapor():
    r_s.show()

def calisma_sayfasi():
    if calisma_s.girdi!=0:
       calisma_s.girdi-=1
    ana_pencere.close()
    calisma_s.show()
    calisma_s.sifre_ayarlar.triggered.connect(sifre_ayarlar_gir)
    calisma_s.bildirim_ayarlar.triggered.connect(bildirim_ayarlar_gir)
    calisma_s.guvenlik_ayarlar.triggered.connect(guvenlik_ayarlar_gir)
    calisma_s.hakkimizda.triggered.connect(hakkimizda)
    calisma_s.buton_geri.clicked.connect(geri_ana_sayfa)
    
    
    calisma_s.notlar.setText(d_i.dosya_oku("notlar.txt"))
  
def ana_sayfa():
    ana_pencere.show()
    ana_s.buton_geri.clicked.connect(geri_giris)
    ana_s.buton_notlar.clicked.connect(notlar)
    ana_s.buton_calisma.clicked.connect(calisma_sayfasi)
    ana_s.buton_rapor.clicked.connect(rapor)
    ana_s.sifre_ayarlar.triggered.connect(sifre_ayarlar_gir)
    ana_s.bildirim_Ayarlar.triggered.connect(bildirim_ayarlar_gir)
    ana_s.actionG_venlik_Ayarlari.triggered.connect(guvenlik_ayarlar_gir)
    ana_s.hakkimizda.triggered.connect(hakkimizda)
    
if __name__ == "__main__":
    uygulama = QApplication([])

    giris_s = Giris_Sayfasi()
    ana_pencere = QMainWindow()
    ana_s = Ana_Sayfa()
    ana_s.setupUi(ana_pencere)
    not_s = Notlar()
    s_a = Sifre_Ayarlari()
    b_a = Bildirim_Ayarlari()
    g_a = Guvenlik_Ayarlari()
    
    hakkimizda_pencere = QMainWindow()
    h_s = Hakkimizda()
    h_s.setupUi(hakkimizda_pencere)
    
    r_s = Rapor()
    calisma_s=Calisma_sayfasi()
    
    
    giris()
    
    uygulama.exec_()
    tahmin.tahmin()
    