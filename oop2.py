import time
import random

renkler = ["Siyah","Beyaz","Gri","Lacivert"]

class Araba:
    def __init__(self,beygirGucu,motorGucu,renk,km):
        self.beygirGucu = beygirGucu
        self.motorGucu = motorGucu
        self.renk = renk
        self.km = km

    # str : print icerisinde overriding
    # overriding : eski fonksiyonu geçersiz kılmak
    def __str__(self):
        return "Beygir Gücü: {}\nMotor Gücü: {}\nRenk: {}\nKm: {}".format(self.beygirGucu,self.motorGucu,self.renk,self.km)
    def __len__(self):
        print("km hesaplanıyor...")
        time.sleep(2)
        return self.km
    def __del__(self):
        print("araba siliniyor...")
        time.sleep(2)
        print("araba silindi")

    def kmArttir(self,deger):
        self.km += deger

    def renkDegis(self,colour):
        self.renk = colour

    def rastgeleRenkDegistir(self,renkler):
        rastgeleRenkIndex = random.randint(0,len(renkler)-1)
        self.renk = renkler[rastgeleRenkIndex]

    def motorGucuArttir(self,gucDegeri):
        self.motorGucu += gucDegeri

    def beygirGucuArttir(self,beygirDegeri):
        self.beygirGucu += beygirDegeri

    def kmSifirla(self):
        self.km = 0

araba1 = Araba(700,3500,"siyah",15000)

while True:
    print("""
    1- araba bilgilerini getir.
    2- arabanın Km bilgisini getir
    3- Arabayı sil
    4- arabanın motor gücünü arttır
    5- arabanın beygir gücünü arttır
    6- arabanın km bilgisini sıfırla
    7-arabanın km bilgisini arttır
    8- arabanın rengini değiştir
    9- arabanın rengini rastgele değiştir
    0- Çıkış
    """)

    secim = int(input("İşlem numaranızı kodlayınız: "))

    if secim == 0:
        print("Çıkış yaptınız")
        break
    if secim == 1:
        print(araba1)
    elif secim == 2:
        print(len(araba1))
    elif secim == 3:
        del araba1
        print("araba silindiği için işlem sonlandırıldı")
        break
    elif secim == 4:
        gucDegeri = int(input("aracın yeni motor gücüne eklemek istediğiniz gücü giriniz: "))
        araba1.motorGucuArttir(gucDegeri)
        print("aracın yeni motor gücü",gucDegeri)
    elif secim == 5:
        beygirDegeri = int(input("aracın beygirine gücüne eklenecek gücü giriniz: "))
        araba1.beygirGucuArttir(beygirDegeri)
        print("aracın yeni beygir gücü",beygirDegeri)
    elif secim == 6:
        print("km bilgisi sıfırlanıyor...")
        time.sleep(2)
        print("km bilgisi başarıyla sıfırlandı")
        araba1.kmSifirla()
    elif secim == 7:
        deger = int(input("eklenecek değeri yaznız: "))
        araba1.kmArttir(deger)
        print("Aracın km bilgisi {} arttırıldı".format(deger))
    elif secim == 8:
        colour = input("yeni rengi yazınız: ")
        araba1.renkDegis(colour)
        print("aracın yeni rengi",colour)
    elif secim == 9:
        araba1.rastgeleRenkDegistir(renkler)
        print("araba, rastgele {} rengine boyandı".format(araba1.renk))
    else:
        print("hatalı tuşlama yaptıınız...")
        break