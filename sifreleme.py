import hashlib
import dosya_islemleri as dsi

def sifrele(sifrelenecekMetin):
    return str(hashlib.md5(sifrelenecekMetin.encode("utf-8")).hexdigest())

def sifremi_ayarla(ayarlanacak_metin,dosya):
    """
    Bu fonksiyonun gorevi parametre olarak alinan metni, giris bilgisinin
    tutulacagi "dosya" parametresiyle alinan dosyaya yazmaktir.
    """
    dsi.dosyaya_yaz(sifrele(ayarlanacak_metin),dosya)

def desifrele(kontrol_edilecek_bilgi,dosya):
    """
    Bu fonksiyonun gorevi parametre olarak aldigi metinle,
    "dosya" parametresiyle alinan dosyada yazili olan giris bilgisini
    karsilastirmaktir.
    """
    tutulan_sifre = dsi.dosya_oku(dosya)
    if str(sifrele(kontrol_edilecek_bilgi)) == tutulan_sifre:
        return True
    else:
        return False
