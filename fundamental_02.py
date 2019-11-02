#segitiga 1
alas = 2
tinggi = 5

luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

#segitiga 2
alas = 7
tinggi = 2

luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

#SEDERHANAKAN DENGAN MEMBUAT FUNGSI
def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

segitiga1 =  hitung_luas_segitiga(10, 2)
print(segitiga1)
segitiga2 =  hitung_luas_segitiga(30, 2)
print(segitiga2)

segitiga3 =  hitung_luas_segitiga(10, 2)
print(segitiga3)

#OOP / CLASS
"""
1. Encapsulation
2. Inheritance
3. Polymorphisme
"""


# ENCAPSULATION => dMembuat class (gabungan antara variabel dan fungsi)
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

    def is_segitiga_sama_sisi(self):
        pass

class SegitigaSamaSisi(Segitiga):
    def is_segitiga_sama_sisi(self):
        return True

class SegitigaSamaKaki(Segitiga):
    def is_segitiga_sama_sisi(self):
        return False

segitiga1 = Segitiga(10, 4)
print(segitiga1.alas)
print(segitiga1.hitung_luas())

sama_kaki = SegitigaSamaKaki(10,10)
print(sama_kaki.is_segitiga_sama_sisi())

sama_sisi = SegitigaSamaSisi(90, 20)
print(sama_sisi.is_segitiga_sama_sisi())



