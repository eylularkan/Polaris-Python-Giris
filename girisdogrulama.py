import re

def sifre_guclu_mu(password: str) -> bool:
    pattern = re.compile(
        r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).+$"
    )
    return bool(pattern.match(password))


if __name__ == "__main__":
    password = input("Lütfen bir şifre giriniz: ")

    if sifre_guclu_mu(password):
        print("✓ Şifre güçlü. Giriş onaylandı.")
    else:
        print("X Şifre zayıf!")
        print("Şifre en az 1 büyük harf, 1 rakam ve 1 özel karakter içermelidir.")
    
# test_guvenlik dosyasına geç kontrol et 