from PyQt5.QtWidgets import QMainWindow,QMessageBox
import dosya_islemleri as d_i
import bildirimler as bildir
from bildirim_ayarlari_arayuz import Ui_MainWindow as bil_ayar
class Bildirim_Ayarlari(QMainWindow):
    """"Bildirim ayari arayuzunu olusturdugumuz ve zamanlayicida sure bitince verilecek bildirimin turunun kullanici
    tarafindan secilmesini saglayan ve bu bilgiyi tutan bildirim ayari sinifi
    """
    def __init__(self):
        super(Bildirim_Ayarlari,self).__init__()
        self.basla()
    def basla(self):
        """Arayuzu olusturuyoruz,butonu etkinlestiriyoruz"""
        self.ui = bil_ayar()
        self.ui.setupUi(self)
        self.baglantilar()
    def bildirim_turu(self):
        """ Kullanicinin sectigi bildirim turunu sonradan okuyup kontrol etmek icin txt dosyasına kaydediyoruz
        """
        bildirim=self.ui.comboBox_bildirim.currentText()
        if bildirim == "Sesle Bildirim Almak Istiyorum":
            d_i.dosyaya_yaz("1","bildirim_turu.txt")
        else:
            d_i.dosyaya_yaz("0","bildirim_turu.txt")
        bildir.mesaj_bildirim("Bilgilendirme", "Bildirim turu ayarlandi")
            
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
    def baglantilar(self):
        """
        Bu fonksiyonun gorevi arayuzdeki butonlari dinlemektir.
        Ve eger bu butonlardan birine tiklandiysa gerekli fonksiyona yonlendirir.
        kaydet butonuna basinca bildirim_turu fonksiyonuna yonlendiriyor
        """
        self.ui.buton_kaydet.clicked.connect(self.bildirim_turu)
