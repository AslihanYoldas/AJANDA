import os
def Path(dosya):
    "Dosyanin bilgisyarda bulundugu konumu doner"
    dosya_yolu = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dosya_yolu, dosya)
def dosyaya_yaz(yazilacak_metin,dosya):
    """Parametre olarak yazilacak metini ve dosyanın adinı alir. Ismi verilen 
    dosyayi açar o metni yazar ve dosyayi kapatir"""
    with open(Path(dosya),mode='w') as yazilacak_dosya:
        yazilacak_dosya.write(yazilacak_metin)            
def dosya_oku(dosya):
    """Parametre olarak dosyanın adini alir. Adi verilen 
    dosyayi açar. Dosyayi okunan degiskenine okur ve dosyayi kapatir. okunani geri dondurur. """
    with open(Path(dosya),mode='r') as okunacak_dosya:
        okunan = okunacak_dosya.read()
    return okunan
def dosyaya_yaz_metinler(metinler,dosya):
    "tuple olarak aldigi metinler degiskenindeki elemanlari dosyaya yazar ve her elemandan sonra ',' koyar. Yani elemanlari , ayraci ile ayiririz "
    with open(Path(dosya),mode='w') as yazilacak_dosya:
        for i in metinler:
            yazilacak_dosya.write(str(i)+',')    
def dosya_oku_metinler(dosya):
    "Dosyadaki metini okuyor ve virgul ayiracindan elemanlara ayirip listeye atiyor .Bu listeyi donduruyor"
    with open(Path(dosya),mode='r') as okunacak_dosya:
        okunan = okunacak_dosya.read()
        okunan=str(okunan).split(',')
    return okunan
