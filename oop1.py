import time

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


araba1 = Araba(700,3500,"siyah",15000)
print(araba1) # methodlar dönen bilgiler geldi.
print("Arabanın KM'si: ",len(araba1)) # __len__ methodunun değeri döndürüldü

print("arabayı silmek istiyor musunuz?")

print("""
1- Evet
0-Hayır
""")

secim = int(input("Tuşlama yapınız..."))

if secim == 1:
    del araba1

elif secim == 0:
    print("araba silme işlemi iptal edildi")

else:
    print("hatalı tuşlama yaptınız")