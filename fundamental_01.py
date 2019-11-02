"""
Esensi sintaksis Python:
- Sequential
- Branching / Percabangan
- Loop / Perulangan
- Tipe data penting: List dan Dictionary
- Modularization dengan:
- a. Fungsi
- b. Class
- c. Package

Program yang akan dibuat: adalah blog dengan Django
"""
judul = 'Menguasai Python dalam 3 Jam'
author = 'Eko Wibowo'
tanggal = '2009-11-02'

jumlah_artikel = 70

# TUGAS: Tampilkan kata2: Kecil, Menengah dan Besar
# Kecil jika nilai 0 - 10
# Menengah jika nilai 11 - 30
# Besar jika lebih besar dari 30
if jumlah_artikel >= 100:
    print('Jumlah artikel besar, akan dipaginasi')
elif jumlah_artikel > 20 and jumlah_artikel <= 60:
    print('Menengah')
else:
    print('Artikel cukup kecil, tidak perlu paginasi')

#PERULANGAN
for i in range(1, 11):
    print(i)

#Cetak angka dari suatu variabel bebas s/d 1 menurun
angka = 15
while angka >= 1:
    print(angka)
    angka = angka - 1

#Dynamically Typed Language => JavaScript
angka = 'Lima Belas'
print(angka)

#TIPE DATA LIST / ARRAY
jenis_kelamin = ['Pria', 'Wanita']
for jk in jenis_kelamin:
    print(jk)

#TIPE DATA BEBASS!
angka = [1, 'loro', 3, 4.0, True]
for a in angka:
    print(a)

#DICTIONARY / JSON
kamus_cinta = {}
kamus_cinta['love'] = 'tresna'
kamus_cinta['sayang'] = 'kangen'
print(kamus_cinta['love'])

manusia = [
    {
    'nama': 'Eko Wibowo',
    'alamat': {
        'line 1': 'Glagah Kidul RT 3',
        'Kelurahan': 'Tamanan',
        'Kecamatan': 'Banguntapan',
        'Kota': 'Bantul',
        'Provinsi': 'DIY'
    }},
    {
        'nama': 'Agus',
        'alamat': {
            'line 1': 'Glagah Kidul RT 3',
            'Kelurahan': 'Tamanan',
            'Kecamatan': 'Banguntapan',
            'Kota': 'Bantul',
            'Provinsi': 'DIY'
        }},
]
print(manusia[0]['nama'])
print(manusia[0]['alamat']['line 1'])
print(manusia[0]['alamat']['Kelurahan'])

