class Dedektif:
    def __init__(self):
        # Başlangıç şüphelileri 
        self.supheliler = ["Albay Mustard", "Profesör Plum", "Bayan Scarlet"]

    def supheli_ele(self, isim):
        if isim in self.supheliler:
            self.supheliler.remove(isim)
            print(f"{isim} elendi.")
        else:
            print(f"{isim} zaten listede yok veya daha önce elenmiş.")

    def suclu_kim(self):
        if len(self.supheliler) == 1:
            print(f"Kesin bilgi, suçlu bulundu: {self.supheliler[0]}")
        elif len(self.supheliler) > 1:
            print("Henüz yeterli kanıt yok.")
        else:
            print("Mantık hatası: Herkes elendi!")



# TEST

d = Dedektif()

d.suclu_kim()  
# Henüz yeterli kanıt yok.

d.supheli_ele("Albay Mustard")
d.suclu_kim()  
# Henüz yeterli kanıt yok.

d.supheli_ele("Profesör Plum")
d.suclu_kim()  
# Kesin bilgi, suçlu bulundu: Bayan Scarlet