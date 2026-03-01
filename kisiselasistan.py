class Asistan:
    def __init__(self, isim):
        self.isim = isim
        self.islem_sayisi = 0  # Başlangıçta 0

    def selam_ver(self, kullanici_adi):
        print(f"Merhaba {kullanici_adi}, ben {self.isim}. Sana nasıl yardım edebilirim?")
        self.islem_sayisi += 1  # Her çağrıldığında 1 artar

    def durum_raporu(self):
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")



# TEST

# Asistan nesnesi oluştur
asistan1 = Asistan("EYLÜL-AI")

# Birkaç kez selam ver
asistan1.selam_ver("Aslı")
asistan1.selam_ver("Yaren")
asistan1.selam_ver("Beren")

# Durum raporu al
asistan1.durum_raporu()