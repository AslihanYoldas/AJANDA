from PyQt5.QtWidgets import QMainWindow,QWidget,QGridLayout
import pyqtgraph as pg
import pandas as pd
import dosya_islemleri as d_i
  
class Rapor(QMainWindow):
    """Haftalik calisma grafigini gosteren bir pencere olusturuyoruz. Qt Designer kullanmadan kendimiz 
    PytQ5 ile bu pencereyi olusturuyoruz"""
    def __init__(self):
        """Tum isi yapan basla fonksiyonunu cagriyoruz ve show ile olusturdugumuz bar grafigini gosteriyoruz """
        super().__init__()
        self.setWindowTitle("Haftalik Rapor")
        self.setGeometry(100, 100, 600, 500)
        self.basla()
  
    def basla(self):
        """Grafigi gosterecek widget i olusturuyoruz.Grafik icin pandas kutuphanesini kullanarak csv dosyadan bulundugumuz 
       haftanin gunlere gore ders calisma surelerini okuyoruz ve bu verilere gore bar grafigini olusturuyoruz.Widget a 
       grafigi ekliyoruz ve pencerede gosterilmesini sagliyoruz"""     
        widget = QWidget()
        plot = pg.plot()
        hafta_sayisi=d_i.dosya_oku("hafta_numarasi.txt")
        hafta_sayisi=int(hafta_sayisi)-1
        data=pd.read_csv(d_i.Path("veriler.csv"),sep=';',names=["Pzt","Salı","Çrş","Prş","Cuma","Cmrts","Pazar"])
        x=[1,2,3,4,5,6,7]
        y=data.loc[hafta_sayisi].values
        plot.setLabel('bottom', ' <p style="font-size:15px;color:green">Haftanin Gunleri(1:Pzt 2:Sali 3:Crs 4:Prs 5:Cuma 6:Cmt 7:Pzr) </p>')
        plot.setLabel('left',' <p style="font-size:15px;color:green">Calisma Sureleri(Saat)</p>')
        plot.setTitle(' <p style="font-size:15px;color:green">Haftalik Calisma Grafigi</p>')
        plot.setBackground('d5ecf2')
        bargraph = pg.BarGraphItem(x = x, height = y, width = 0.6, brush ='b') 
        plot.addItem(bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(plot)
        self.setCentralWidget(widget)
  