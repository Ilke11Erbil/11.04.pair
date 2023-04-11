class Ogrenci:
    def __init__(self,ad, soyad, numara, sinif):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.sinif = sinif


    def ogrenci_bilgilerini_goster(self):
        print(f"Adı: {self.ad}\nSoyadı: {self.soyad}\nOkul Numarası: {self.numara}\nSinif: {self.sinif}")

    