from PyQt5 import QtCore 
from PyQt5.QtWidgets import  QMainWindow,QMessageBox
import time
import dosya_islemleri as d_i
import bildirimler as bildir
from calisma_sayfasi_arayuz import Ui_MainWindow as calisma_sayfasi
import PyQt5.QtWidgets as QtWidgets
import sqlite3
import veri_islemleri

class Calisma_sayfasi(QMainWindow,calisma_sayfasi):
    """Calisma sayfasindaki haftalik program ,zamanlayici, yapilacaklar listesinin calismasini saglayan sinif"""
    def __init__(self):
        """Arayuzu olusturuyoruz.Butonlari etkinlestiriyoruz.Zamanlayiciyi sifirliyoruz.100 milisaniyede bir geri_sayim fonksiyonunu cagriyoruz
        Sinif degiskenlerine ilk degerlerini atiyoruz"""
        super(Calisma_sayfasi,self).__init__()
        self.calisma=0#calisma suresi
        self.ara=0#ara suresi
        self.toplam_sure_calisma=0#calisma suresi saniye olarak
        self.toplam_sure_ara=0#ara suresi saniye olarak
        self.say=False#Zamanlayici calisiyor mu
        self.devam=False#Zamanlayici ilk mi baslatildi durdurup mu baslatildi bilgisini tutuyor.
        self.baglanti = None
        self.imlec = None
        self.tablo_adi = None
        self.veri = None
        self.tablo_ = []
        self.sutunlar = []
        self.girdi=0
        self.basla()
        self.zaman_sifirla()
        zamanlayici=QtCore.QTimer(self)
        zamanlayici.timeout.connect(self.geri_sayim)
        zamanlayici.start(100)
    
    def closeEvent(self, event):
        """Calisma sayfasindan cikarken yani'X' basilmissa bildirim verip yapilan degisiklikler kaydedilsin mi
        diye soruyor. Save'e basilirsa notlar ve yapilacaklar listesinde yapilan degisiklikler kaydedilir
        close a basarsa kaydetmeden kapanir cancel a basarsa sayfa kapanmaz"""
        if self.girdi==0:
            cevap = QMessageBox.question(
                    self, "Kaydet",
                    "Degisiklikler kaydedilsin mi?",
                    QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
                    QMessageBox.Save)
   
            if cevap == QMessageBox.Close:
                event.accept()
                self.girdi+=1
            elif cevap==QMessageBox.Save:
                d_i.dosyaya_yaz(self.notlar.toPlainText(),("notlar.txt"))
                d_i.dosyaya_yaz_metinler(self.yapilacaklar_listesi_oku(),"yapilacaklar_listesi.txt")
                d_i.dosyaya_yaz(self.yapilacak_listesi_check_box_oku(),"check_box.txt")
                event.accept()
                self.girdi+=1
            else:
                event.ignore()
                self.girdi+=1
            

    def temizle_tablo(self):
        """Arayuzdeki QTableWidget'i tum verilerden temizleyen fonksiyon"""
        self.haftalik_program.clear()
        
    def guncel_tablo(self):
        """
        Uygulama kullanilirken yapilan islemler sonucunda veri tabani degismis olur.
        Bu sebeple islemler sonrasinda bu fonksiyon cagrilarak QTableWidget'e veri tabaninin
        guncel hali yansitilir.
        """
        self.imlec.execute("SELECT * FROM {ta}".format(ta=self.tablo_adi[0][0]))
        self.veri = self.imlec.fetchall()
        self.tablo_ = [[str(j) for j in i] for i in self.veri]
        #Burada "self.tablo_" her haftayi bir elemani olarak tutan bir listedir.
        self.sutunlar = [i[0] for i in self.imlec.description]
        for satir_say, satir_veri in enumerate(self.veri):
            for sutun_say, self.veri in enumerate(satir_veri):
                self.haftalik_program.setItem(satir_say,sutun_say,QtWidgets.QTableWidgetItem(str(self.veri)))
    
    def sutun_sayisi_hesapla(self):
        """Veri tabanindaki tablonun sutun sayisini donduren fonksiyondur."""
        sutun_sorgusu = "PRAGMA table_info(%s)" % self.tablo_adi[0][0]
        self.imlec.execute(sutun_sorgusu)
        return len(self.imlec.fetchall())
    
    def veri_cek(self):
        """
        Bu fonksiyonda once tablonun arayuzdeki son hali, gunleri ve haftalari(satir ve sutun indeksleri)
        duzenli olacak sekilde bir listede tutulur. Sonra veri tabanindaki tablo ile yapilan karsilastirma sonucu
        farkli olan kisimlar veri tabanina islenir.
        """
        try:
            veriler = []
            for satir in range(len(self.tablo_)):#Bu ic ice iki dongu sayesinde QTableWidget'ten sirali veri cekilicek.
                veri_satir = []
                for sutun in range(self.sutun_sayisi_hesapla()):
                    parcacik = self.haftalik_program.item(satir, sutun)
                    veri_satir.append(parcacik.text())
                #Burada "veri_satir" tablodaki bir satiri tutar (Yani bir haftanin verilerini tutar).
                veriler.append(veri_satir)
            #Buradan sonra arayuzdeki tablo ile veri tabanindaki tablo karsilastirilarak degisim yapilan ilk yer yakalanir.
            for asil, duzenlenmis in zip(self.tablo_, veriler):
                if asil != duzenlenmis:
                    for index, (i, j) in enumerate(zip(asil, duzenlenmis)):
                        if i != j:
                            sorgu = f"UPDATE {self.tablo_adi[0][0]} SET " \
                                f"{self.sutunlar[index]} = ? " \
                                f"WHERE {self.sutunlar[1]} = ?"
                            self.imlec.execute(sorgu, (j, asil[1]))
            self.baglanti.commit()
        except Exception :
            bildir.mesaj_bildirim("Uyari","Lutfen uygulamayi yeniden acin! Yapılan degisikler su anda kaydedilememektedir.")

    def degistir(self):
        """
        Bu fonksiyon QTableWidget'teki bir kutunun icindeki veriyi degistirme isleminin akisini icerir.
        """
        self.veri_cek()
        self.temizle_tablo()
        self.guncel_tablo()
    
    def sil(self):
        """
        Bu fonksiyon kullanicinin bir satiri silmesini saglar.(Yani bir hafta silme gorevini gorur.)
        """
        silinecek_satir = self.haftalik_program.selectedItems()
        secilen = silinecek_satir[0].text()
        sorgu_silme = ("DELETE FROM {} WHERE {} = ?".format((self.tablo_adi[0][0]),(self.sutunlar[0])))
        self.imlec.execute(sorgu_silme,(secilen,))
        self.baglanti.commit()
        self.temizle_tablo()
        self.guncel_tablo()
    
    def ekle(self):
        """
        Bu fonksiyonda veri tabanina yeni bir satir(hafta) eklenir.
        Bu ekleme islemi sonucunda arayuzde varsayilan metin olarak ayarladigimiz 
        "Bugun ne yapsam?" yazar. Bu yeni haftaya veri girecek kullanici burdan sonra "Degistir"
        butonuyla varsayilan metni istedigi metin ile degistirebilir.
        """
        gecici_satir_verisi = []
        for x in range(self.sutun_sayisi_hesapla()):
            gecici_satir_verisi.append("Bugun ne yapsam?")
        self.imlec.execute(f"INSERT INTO {self.tablo_adi[0][0]} VALUES({', '.join('?' * self.sutun_sayisi_hesapla())})",gecici_satir_verisi)
        self.baglanti.commit()
        self.temizle_tablo()
        self.guncel_tablo()
    
    def tavsiye(self):
        """
        Uygulama kullanicinin gun bazinda calisma verilerini tutar ve tavsiye istendiginde bu fonksiyon araciligiyla
        haftanin hangi kisminda daha cok calistiysa ona uygun bir tavsiye verir.
        """
        ilk = veri_islemleri.hafta_ilk_yari_ort()
        son = veri_islemleri.hafta_ikinci_yari_ort()
        if ilk > son :
            bildir.mesaj_bildirim("Tavsiye","Calisirken seni takip ettim ve fark ettim ki hafta ici daha iyi calisiyorsun. Gelecek hafta ki planlamani buna gore yapmani tavsiye ederim.")
        elif son > ilk:
            bildir.mesaj_bildirim("Tavsiye","Belli ki tatil seni motive ediyor, bu haftaki programini hafta sonu yogunluklu yapmani tavsiye ederim.")
        else:
            bildir.mesaj_bildirim("Tavsiye","Genelde hafta boyunca dengeli calisiyorsun gibi gozukuyor, o zaman boyle devam.")
    def dosya_yukle(self):
        """
        Uygulama klasorundeki 'haftalik_program.db' veritabaniyla sql sorgu dili araciligiyla baglanti kurup,
        bu veritabanindaki verileri arayuzdeki QTableWidget'e bastiran fonksiyondur.
        """
        self.baglanti = sqlite3.connect(d_i.Path("haftalik_program.db"))
        self.imlec = self.baglanti.cursor()
        self.imlec.execute("SELECT name FROM sqlite_master")
        self.tablo_adi = self.imlec.fetchall()
        
        if self.tablo_adi == []:
            bildir.mesaj_bildirim("AJANDA","Haftalik programin bos gozukuyor, doldurmaya ne dersin?")
        else:
            self.temizle_tablo()
            self.imlec.execute("SELECT * FROM {ta}".format(ta=self.tablo_adi[0][0]))
            self.veri = self.imlec.fetchall()
            self.tablo_ = [[str(j) for j in i] for i in self.veri]
            self.sutunlar = [i[0] for i in self.imlec.description]
            for satir_say, satir_veri in enumerate(self.veri):
                for sutun_say, self.veri in enumerate(satir_veri):
                    self.haftalik_program.setItem(satir_say,sutun_say,QtWidgets.QTableWidgetItem(str(self.veri)))
        
    
    def basla(self):
        self.setupUi(self)
        self.baglantilar()   
        self.yapilacaklar_listesi_yaz()
        self.yapilacak_listesi_check_box_yaz()
        self.dosya_yukle()
        self.buton_degistir.clicked.connect(self.degistir)
        self.buton_sil.clicked.connect(self.sil)
        self.buton_hafta_ekle.clicked.connect(self.ekle)
        self.buton_tavisye.clicked.connect(self.tavsiye)
        
        """Burdan sonrasi zamanlayici ile ilgili kodlar. Zamanlayici secilen calisma ve ara zamanina gore geri sayim yapiyor
        Zamanlayiciyi baslatma,durdurma ve sureyi sifirlama ozelliklerine sahip.Calisma suresi bitince ara suresi otomatik
        olarak basliyor.Calisma ve ara suresi bittiginde seciminize gore sesli veya pencere olarak bildirim veriyor"""
    def zaman_basla(self):
        """basla butonuna basinca calisan fonksiyon.Zamanlayiciyi baslatiyor."""
        if self.say==False :
            self.say=True
            if self.devam!=True:
                self.calisma,self.ara=self.zamani_ayarla()
                self.toplam_sure_calisma=self.calisma*60
                self.toplam_sure_ara=self.ara*60     
    def zaman_durdur(self):
        """Zamanlayiciyi durduruyor"""
        self.say = False
        self.devam=True
        
    def zaman_sifirla(self):
        """Zamanlayiciyi sifirliyor"""
        self.say = False
        self.label_zamanlayici.setText("00:00")
        self.calisma = 0
        self.ara=0
        self.dakika=0
        self.saniye=0
    def zamani_goster(self,sure):
        """Toplam saniye olarak sureyi aliyor ve ekrana dakika ve saniye cinsinden surenin yazilmasini sagliyor"""
        self.dakika=sure//60
        self.saniye=sure%60
        self.label_zamanlayici.setText(("0"+str(self.dakika) if self.dakika<10 else str(self.dakika))+":"
                                          +("0"+str(self.saniye)if self.saniye<10 else str(self.saniye)))
     
    def geri_sayim(self):
        """Zamanlayicida geri sayim isleminin yapilmasini sağlayan kisim.Bu fonksiyon 100 ms de bir cagriliyor ve surenin
        azalmasi ve ekrana gosterilmesi saglaniyor.Ilk once calisma suresi geriye sayiliyor o bitince bildirim verilmesi saglanip
        ara suresi geriye sayiliyor.O bitince de tekrar bildirim veriliyor.Calisma suresi bitince toplam calisma suresinin tutuldugu dosya guncelleniyor"""
        if self.say==True:
            if self.devam==True:
                self.zamani_goster(self.dakika*60+self.saniye)
                self.devam=False  
            self.zamani_goster(self.toplam_sure_calisma)
            time.sleep(1)
        if self.say==True:
                self.toplam_sure_calisma-=1
                if self.toplam_sure_calisma==0:
                        self.label_zamanlayici.setText("00:00")
                        self.zamanlayici_bildirim("Ara Zamani","Calisma zamani bitti. Mola zamani")
                        self.gunluk_sayac()
                        self.calisma=0
        if self.calisma==0 and self.ara :
            self.zamani_goster(self.toplam_sure_ara)
            time.sleep(1)
            if self.say==True:
                    self.toplam_sure_ara-=1
                    if self.toplam_sure_ara==0:
                            self.say=False
                            self.label_zamanlayici.setText("00:00")
                            self.zamanlayici_bildirim("Ara Bitti","Mola bitti.Bir donguyu tamamladin.Calismaya devam etmek istiyorsan zamanlayiciyi tekrar baslat")
                            self.ara=0
    def zamani_ayarla(self):
        """Kullanicinin sectigi secenege gore calisma ve ara sureleri guncelleniyor"""
        zaman_turu=self.islem_sec_2.currentText()
        if(zaman_turu=="25/5"):
            return 25,5
        elif(zaman_turu=="40/10"):
            return 40,10
        else:
            return 60,10  
    def zamanlayici_bildirim(self,pencere_basligi,mesaj):
        """Kullanicinin sectigi bildirim turune gore o ilgili bildirim fonksiyonu cagriliyor"""
        bildirim=d_i.dosya_oku("bildirim_turu.txt")
        if bildirim=='1':
            bildir.sesli_bildirim()
        else:
            bildir.mesaj_bildirim(pencere_basligi,mesaj)
    def gunluk_sayac(self):
        """Gunluk olarak kullanicinin toplam calisma suresini guncelleyip dosyaya yazan fonksiyon"""
        gunluk_toplam=d_i.dosya_oku("gunluk_calisma.txt")
        temp=int(gunluk_toplam)
        temp+=self.calisma
        d_i.dosyaya_yaz(str(temp),"gunluk_calisma.txt")
    def baglantilar(self):
        """Butonlari fonksiyonlara bagliyoruz"""
        self.buton_basla.clicked.connect(self.zaman_basla)
        self.buton_dur.clicked.connect(self.zaman_durdur)
        self.buton_reset.clicked.connect(self.zaman_sifirla)
        
        #Yapilacaklar Listesi
    def yapilacaklar_listesi_oku(self):
        """Yapilacaklar listesine yazilanlari okuyup onlari tuple olarak donduruyor"""
        metin1=self.yapilacak1.text()
        metin2=self.yapilacak2.text()
        metin3=self.yapilacak3.text()
        metin4=self.yapilacak4.text()
        metin5=self.yapilacak5.text()
        yapilacak_listesi=metin1,metin2,metin3,metin4,metin5
        return yapilacak_listesi
    def yapilacaklar_listesi_yaz(self):
        """Sayfa acildiğinda onceden yazilanlari dosyadan okuyup yapilacaklar listesine yerlestiriyor"""
        yapilacak_listesi=d_i.dosya_oku_metinler("yapilacaklar_listesi.txt")
        self.yapilacak1.setText(yapilacak_listesi[0])
        self.yapilacak2.setText(yapilacak_listesi[1])
        self.yapilacak3.setText(yapilacak_listesi[2])
        self.yapilacak4.setText(yapilacak_listesi[3])
        self.yapilacak5.setText(yapilacak_listesi[4])
    def yapilacak_listesi_check_box_oku(self):
        """Yapilacaklar listesindeki isaretleme kutucuklarinin isaretlenmis olup olmadiklari bilgisini bir string olarak donduruyor"""
        kontrol=''
        check_box=self.check1.isChecked(),self.check2.isChecked(),self.check3.isChecked(),self.check4.isChecked(),self.check5.isChecked()
        for i in check_box:
            kontrol+=( '1' if i==True else '0' )      
            kontrol+=','
        return kontrol
    def yapilacak_listesi_check_box_yaz(self):
        """Sayfa acildiginda onceden isaret kutucuklarin bilgisini tuttugumuz dosyayi okuyup ona göre onceden isaretlenmis kutucuklari isaretliyoruz"""
        check_box=d_i.dosya_oku_metinler("check_box.txt")
        if check_box[0]=='1':
            self.check1.setChecked(True)
        if check_box[1]=='1':
            self.check2.setChecked(True)
        if check_box[2]=='1':
            self.check3.setChecked(True)
        if check_box[3]=='1':
            self.check4.setChecked(True)
        if check_box[4]=='1':
            self.check5.setChecked(True)
                