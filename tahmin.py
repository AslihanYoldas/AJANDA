from scipy import stats
#import  seaborn as sns 
import pandas as pd
import veri_islemleri
import bildirimler 
import dosya_islemleri


def gun_ismi_ayarla():
    """ Yasanan gune gore temsili sayisal degerler donduren fonksiyondur."""
    return veri_islemleri.gun_numarala()
def tahmin_hesapla(lnreg):
    gun_temsil = gun_ismi_ayarla()
    return lnreg.slope * gun_temsil + lnreg.intercept
def donustur_int(donusturulecek):
    """Parametre olarak verilen listeyi hesaplamalarda
    kullanilabilecek formata donusturen fonksiyondur."""
    donusturulecek=donusturulecek.split(",")
    gecici = []
    for i in donusturulecek:
        gecici.append(int(i))
    return gecici
def kontrol(tahmin,veriler):
    """Hesaplanan tahmin, bulunulan gunun ortalamasindan dusuk veya esitse 0,
    buyukse 1 donduren fonksiyondur"""
    ort = veri_islemleri.ortalama_gun(veri_islemleri.bugun())
    if tahmin <= int(ort):
        return 0#çalışmaz diye tahmin ediyor
    else:
        return 1#calisir diye tahmin ediyor.
def tahmin():
    """
    Bu fonksiyon lineer regresyon yontemini kullanarak son yedi haftanin
    ortalama calisma saatlerinin tutuldugu 'ort_veriler.csv' dosyasindan
    cektigi verilerle, 0-7 rakamlari arasinda numaralandirilan gunler arasinda
    iliski kurup olusturdugu katsayilarla istenilen gun icin tahmin yapmak amaciyla 
    bu islevleri gerceklestiren fonksiyonlarin akisini icermektedir.
    """
    veri_islemleri.ort_yaz_dosya()
    veri_seti = pd.read_csv(dosya_islemleri.Path('ort_veriler.csv'), delimiter = ';',header=None, names=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    veri_seti.gunler = [0,1,2,3,4,5,6]#Haftanin gunlerini 0-7 arasi rakamlarla temsil ettik.
    tut = veri_seti.iloc[:2,:].values
    veri_seti.ort_calisma_saatleri = donustur_int(tut[1][0])
    lnreg = stats.linregress(x = veri_seti.gunler,y=veri_seti.ort_calisma_saatleri)
    #sns.set_style('whitegrid')
    #axes = sns.regplot(x = veri_seti.gunler,y=veri_seti.ort_calisma_saatleri)
    if kontrol(int(tahmin_hesapla(lnreg)),veri_seti.ort_calisma_saatleri) == 0:
        bildirimler.masaustu_bildirim("Genelde haftanin bu gununde daha az calisiyorsun. Bugun biraz daha calisarak bunu kirmaya ne dersin?")
