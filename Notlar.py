from PyQt5.QtWidgets import QMainWindow, QMessageBox
import dosya_islemleri as d_i
from notlar_arayuz import Ui_MainWindow as notlar
class Notlar(QMainWindow,notlar):
    """Notlar arayuzunu olusturdugumuz ve notlara kullanicinin yazdigi yazilari kaydettigimiz sinif"""
    def __init__(self):
        super(Notlar,self).__init__()
        self.basla()
    def basla(self):
        """Notlari olusturuyoruz.Notlara onceden kaydedilmis yazılari dosyadan okuyoruz"""
        self.setupUi(self)
        self.notlar.setText(d_i.dosya_oku("notlar.txt"))
    def metin_cek(self):
        """Notlara kullanici tarafından yazilan metni donduruyor"""
        metin=self.notlar.toPlainText()
        return metin
    def closeEvent(self, event):
        """Notlardan cikarken yani'X' basılmıssa bildirim verip yapslan degisiklikler kaydedilsin mi
        diye soruyor. Save'e basslrsa metin_cek fonk ile metin cekilip dosyaya yazilir ve kapanir
        close a basarsa notlar kaydetmeden kapanir cancel a basarsa notlar kapanmaz"""
        cevap = QMessageBox.question(
            self, "Kaydet",
            "Degisiklikler kaydedilsin mi?",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        if cevap == QMessageBox.Close:
            event.accept()
        elif cevap==QMessageBox.Save:
            d_i.dosyaya_yaz(self.metin_cek(),("notlar.txt"))
            event.accept()
        else:
            event.ignore()
        
        
    
        