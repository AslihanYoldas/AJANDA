from PyQt5.QtWidgets  import QMessageBox
import dosya_islemleri as d_i
from win10toast import ToastNotifier
from playsound import playsound

def mesaj_bildirim(pencere_basligi,mesaj):
    """Ekrana basit bir bildirim verir. Parametre olarak pencerenin basligini ve mesaji alir.Mesaji bildirimde yazdirir.
    Sadece "ok" secenegi olur yani kullaniciya herhangi bir durumla ilgili bilgi veya uyari verebilir."""
    kutu=QMessageBox()
    kutu.setWindowTitle(pencere_basligi)
    kutu.setText(mesaj)
    buton_tamam=kutu.button(QMessageBox.Ok)
    kutu.exec_()
 
def masaustu_bildirim(mesaj):
    """Parametre olarak verilen mesaji kullanicinin ekranina masaustu bildirimi olarak donduren fonksiyondur."""
    bildirim = ToastNotifier() 
    bildirim.show_toast(title='AJANDA', msg=mesaj, icon_path=d_i.Path("ikon.ico"), duration=20)

def sesli_bildirim():
    """Cagrildigi durumda ses ile bildirim veren fonksiyondur."""
    playsound(d_i.Path('ses.mp3'))
        