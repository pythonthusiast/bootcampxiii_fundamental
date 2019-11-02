class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

    def is_segitiga_sama_sisi(self):
        pass