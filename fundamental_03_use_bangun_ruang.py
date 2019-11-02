from bangunruang.segitiga_base import Segitiga
from bangunruang.segitiga_sama_kaki import SegitigaSamaKaki
from bangunruang.segitiga_sama_sisi import SegitigaSamaSisi

segitiga1 = Segitiga(10, 4)
print(segitiga1.alas)
print(segitiga1.hitung_luas())

sama_kaki = SegitigaSamaKaki(10, 10)
print(sama_kaki.is_segitiga_sama_sisi())

sama_sisi = SegitigaSamaSisi(90, 20)
print(sama_sisi.is_segitiga_sama_sisi())