# import math

# class BangunRuang:
#     def hitung_volume(self):
#         pass

# class Kubus(BangunRuang):
#     def __init__(self, sisi):
#         self.sisi = sisi

#     def hitung_volume(self):
#         return self.sisi ** 3

# class Balok(BangunRuang):
#     def __init__(self, panjang, lebar, tinggi):
#         self.panjang = panjang
#         self.lebar = lebar
#         self.tinggi = tinggi

#     def hitung_volume(self):
#         return self.panjang * self.lebar * self.tinggi

# class Tabung(BangunRuang):
#     def __init__(self, jari_jari, tinggi):
#         self.jari_jari = jari_jari
#         self.tinggi = tinggi

#     def hitung_volume(self):
#         return math.pi * self.jari_jari ** 2 * self.tinggi

# kubus = Kubus(5)
# print("Volume Kubus:", kubus.hitung_volume())

# balok = Balok(3, 4, 5)
# print("Volume Balok:", balok.hitung_volume())

# tabung = Tabung(2, 7)
# print("Volume Tabung:", tabung.hitung_volume())

# kompetensi 2
class p9e2:
    @staticmethod
    def methodTambah(x, y=None):
        if isinstance(x, int) and isinstance(y, int):
            return p9e2.methodTambahInt(x, y)
        elif isinstance(x, float) and isinstance(y, float):
            return p9e2.methodTambahFloat(x, y)
        else:
            raise TypeError("Tipe data tidak didukung")

    @staticmethod
    def methodTambahInt(x, y):
        return x + y

    @staticmethod
    def methodTambahFloat(x, y):
        return x + y

myNum1 = p9e2.methodTambah(8, 5)
myNum2 = p9e2.methodTambah(4.5, 6.5)
print("int : ", myNum1)
print("float : ", myNum2)
