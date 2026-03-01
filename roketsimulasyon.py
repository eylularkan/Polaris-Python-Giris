class Roket:
    def __init__(self, isim, yakit_seviyesi):
        # başlangıç değerleri
        self.isim = isim
        self.yakit_seviyesi = yakit_seviyesi

    def yakit_doldur(self, miktar):
        # Mevcut yakıta ekleme
        self.yakit_seviyesi += miktar
        print(f"Yakıt eklendi. Yeni seviye: {self.yakit_seviyesi}")

    def firlat(self):
        # Fırlatma kontrolü
        if self.yakit_seviyesi >= 10:
            print("Roket başarıyla fırlatıldı! 🌍 -> 🌕")
            self.yakit_seviyesi -= 10
            print(f"Kalan yakıt: {self.yakit_seviyesi}")
        else:
            print("Hata: Yetersiz yakıt! Lütfen yakıt doldurun.")



# TEST

roket1 = Roket("Apollo 11", 5)

roket1.firlat()        # Yetersiz yakıt hatası 
roket1.yakit_doldur(10)
roket1.firlat()        # Başarılı fırlatma
roket1.firlat()        # Tekrar dene (yakıt kontrolü için)