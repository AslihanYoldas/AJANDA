from PyQt5.QtWidgets import QMainWindow, QMessageBox
import dosya_islemleri as d_i
import bildirimler as bildir
from notlar_arayuz import Ui_MainWindow as notlar
class Notlar(QMainWindow,notlar):
    def __init__(self):
        super(Notlar,self).__init__()
        self.basla()
    def basla(self):
        """Notları oluşturuyoruz.Notlara önceden kaydedilmiş yazıları dosyadan okuyoruz"""
        self.setupUi(self)
        self.notlar.setText(d_i.dosya_oku("notlar.txt"))
    def metin_cek(self):
        """Notlara kullanıcı tarafından yazılan metni döndürüyor"""
        metin=self.notlar.toPlainText()
        return metin
    def closeEvent(self, event):
        """Notlardan çıkarken yani'X' basılmışsa bildirim verip yapılan değişiklikler kaydedilsin mi
        diye soruyor. Save'e basılrsa metincek fonk ile metin çekilip dosyaya yazılır ve kapanır
        close a basarsa notlar kaydetmeden kapanır cancel a basarsa notlar kapanmaz"""
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
        
        
    
        