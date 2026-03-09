# Örnek veri listesi
people = [
    {"name": "Eylül", "age": 19},
    {"name": "Yaren", "age": 20},
    {"name": "Aslı", "age": 21},
    {"name": "Beren", "age": 22},
    {"name": "Alper", "age": 23},
    {"name": "Ceren", "age": 24}
]

# 1️ Yaşı 20’den büyük olanları filtrele
older_than_20 = [person for person in people if person["age"] > 20]
print("Yaşı 20'den büyük olanlar:")
print(older_than_20)

# 2️ İsmi A ile başlayanları filtrele
starts_with_a = [person for person in people if person["name"].startswith("A")]
print("\nİsmi A ile başlayanlar:")
print(starts_with_a)

# 3️ Yaşı 20’den büyük VE ismi A ile başlayanlar
result = [p for p in people if p["age"] > 20 and p["name"].startswith("A")]
print("\nYaşı 20'den büyük ve ismi A ile başlayanlar:")
print(result)