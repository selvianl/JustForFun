class Ders():

    def __init__(self,name,katsayi):
        self.katsayi=katsayi
        self.name = name

    def netHesapla(self):
        while True:
            try:
                self.dogru = int(input(self.name + "Dogru Sayisi:"))
                self.yanlis = int(input(self.name + "Yanlis Sayisi:"))
                assert (self.dogru + self.yanlis <= 40)
                break
            except AssertionError:
                print("40 sorudan fazla giris yapildi. Tekrar Deneyin.")


        print(self.name , "Dogru : ", self.dogru)
        print(self.name , "Yanlis : ", self.yanlis)

        if (self.dogru+ self.yanlis > 40):
            print ("Cok soru girildi")

        else:
            self.bos=(40 - (self.dogru + self.yanlis))
            print(self.name , "Bos : ", self.bos)

            self.net= (self.dogru - (self.yanlis+(self.yanlis/4)))
            print(self.name , "Net :" ,self.net)

            self.netPuan=( self.net*self.katsayi )
            print(self.name , "Puan : ", self.netPuan)

            return self.netPuan

fen=Ders(name="Fen", katsayi=3,)
fen.netHesapla()

sosyal=Ders(name="Sosyal", katsayi=1,)
sosyal.netHesapla()

matematik=Ders(name="Matematik", katsayi=4,)
matematik.netHesapla()

turkce=Ders(name="Turkce", katsayi=3,)
turkce.netHesapla()

total = (fen.netPuan+sosyal.netPuan+turkce.netPuan+matematik.netPuan)
print("Sinav Puaniniz : ", total)