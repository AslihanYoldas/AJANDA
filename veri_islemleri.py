import pandas
import csv
import datetime
import dosya_islemleri as d_i
"""
Haftayi ilk ve son olarak iki kisma ayirdik.
-ilk yari:pazartesi-sali-carsamba-persembe
-son yari:cuma-cumartesi-pazar
"""
veriler = pandas.read_csv(d_i.Path("veriler.csv"), delimiter=';', header=None, names=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
gunluk_veriler = []

def hafta_kontrol():
    """Toplamda yedi haftalik veri tutulacagi icin dosyanin icinde tutulan hafta numara bilgisinin 
    0-7 araliginda olup olmadiginin kontrolu yapilir. Bu fonksiyon hafta numarasini dondurur."""
    hafta_num = d_i.dosya_oku(d_i.Path("hafta_numarasi.txt"))
    hafta_num = hafta_arttir(hafta_num)
    if int(hafta_num) > 6:
        hafta_num = 0
    d_i.dosyaya_yaz(str(hafta_num),d_i.Path("hafta_numarasi.txt"))
    return hafta_num
def hafta_arttir(hafta_num):
    return  int(hafta_num) + 1

def bugun():
    """ Bu fonksiyon cagrildiginda yasanan gunu donduren fonksiyondur."""
    an = datetime.datetime.now()
    gun = datetime.datetime.strftime(an, '%A')
    return gun

def gun_numarala():
    """Yasanan gune gore temsili sayisal degerler donduren fonksiyondur."""
    bugun_ismi = bugun()
    if bugun_ismi == 'Monday':
        return 0
    if bugun_ismi == 'Tuesday':
        return 1
    if bugun_ismi == 'Wednesday':
        return 2
    if bugun_ismi == 'Thursday':
        return 3
    if bugun_ismi == 'Friday':
        return 4
    if bugun_ismi == 'Saturday':
        return 5
    if bugun_ismi == 'Sunday':
        return 6
    
def donustur_saat(sure_dk):
    """Bu fonksiyon parametre olarak aldigi degiskene gerekli hesaplamalari
    yaparak dakika biriminden saat birimine donusturur."""
    sure_saat = int(sure_dk)/60
    if sure_saat < (int(sure_saat)+0.5):
        #Eger tam saatin uzerinden en az yarim saat gecmediyse alt saate yuvarlanir.
        return int(sure_saat)
    else:
        return int(sure_saat)+1
     

def csv_yaz(yazilacak_satir):
    """Bu fonksiyon parametre olarak verilen nesneyi veriler dosyasina yazan fonksiyondur."""
    with open(d_i.Path("veriler.csv"), 'w', newline='') as dosya:
        tut_yaz = csv.writer(dosya, delimiter=';')
        for satir_num in range(7):
            tut_yaz.writerow(yazilacak_satir.loc[satir_num][:])
        
def gunluk_kayit():
    """ Bu fonksiyon gunun sonunda, dosyada tutulan bugunku calisilan suresini
    veriler.csv dosyasina isleyen fonksiyondur."""
    sure = d_i.dosya_oku("gunluk_calisma.txt")
    sure = donustur_saat(sure)
    df = veriler.copy()
    df.loc[hafta_kontrol()][gun_numarala()] = sure
    csv_yaz(df.loc[:][:])

def ort_yaz_dosya():
    """Bu fonksiyon son yedi haftanin verilerine dayanarak gun bazinda hesaplanan
    ortalamalari 'ort_veriler.csv' dosyasina yazan fonksiyondur."""
    ort_1 = ortalama_gun('Monday')
    ort_2 = ortalama_gun('Tuesday')
    ort_3 = ortalama_gun('Wednesday')
    ort_4 = ortalama_gun('Thursday')
    ort_5 = ortalama_gun('Friday')
    ort_6 = ortalama_gun('Saturday')
    ort_7 = ortalama_gun('Sunday')
    gun_ortalamalari = {'Monday':[int(ort_1)],
                        'Tuesday':[int(ort_2)],
                        'Wednesday':[int(ort_3)],
                        'Thursday':[int(ort_4)],
                        'Friday':[int(ort_5)],
                        'Saturday':[int(ort_6)],
                        'Sunday':[int(ort_7)]}
    df = pandas.DataFrame(gun_ortalamalari,columns=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    df.to_csv(d_i.Path("ort_veriler.csv"),index = False, header=True)

def ortalama_gun(gun):
    """Parametre olarak verilen gunun son 7 haftalik verilerinin 
    ortalamasini hesaplayan fonksiyondur."""
    sayilari_ayir(gun)
    return toplam_hesapla()/7

def toplam_hesapla():
    """
    Bu fonksiyonda 'gunluk_veriler'in elemanlarinin toplami dondurulur.
    Yani kayitli olan haftalar boyunca o gun icin toplam calisma saatini dondurur.
    """
    toplam= 0
    for x in range(len(gunluk_veriler)):
        toplam += int(gunluk_veriler[x])
    return toplam

def sayilari_ayir(gun):
    """
    Bu fonksiyonda calisma saati verileri parametre olarak verilen gunun
    verilerini bir liste halinde dondurur.
    """
    gunluk_veriler.clear()
    for k in range(len(veriler)) :
        metin = veriler[gun][k]
        gunluk_veriler.insert(k,metin)

def hafta_ilk_yari_ort():
    """
    Bu fonksiyonla haftanin ilk kisminin calisma saati verilerinin oratalamasi hesaplanir.
    """
    ilk_yari_toplam = 0
    sayilari_ayir('Monday')
    ilk_yari_toplam += toplam_hesapla()
    sayilari_ayir('Tuesday')
    ilk_yari_toplam += toplam_hesapla()
    sayilari_ayir('Wednesday')
    ilk_yari_toplam += toplam_hesapla()
    sayilari_ayir('Thursday')
    ilk_yari_toplam += toplam_hesapla()
    return ilk_yari_toplam/len(veriler)

def hafta_ikinci_yari_ort():
    """
    Bu fonksiyonla haftanin ikinci kisminin calisma saati verilerinin oratalamasi hesaplanir.
    """
    ikinci_yari_toplam = 0
    sayilari_ayir('Friday')
    ikinci_yari_toplam += toplam_hesapla()
    sayilari_ayir('Saturday')
    ikinci_yari_toplam += toplam_hesapla()
    sayilari_ayir('Sunday')
    ikinci_yari_toplam += toplam_hesapla()
    return ikinci_yari_toplam/len(veriler)
