class Ogretmen:
    def __init__(self, ad, soyad, brans, sicil):
        self.ad = ad
        self.soyad = soyad
        self.brans = brans
        self.sicil_no = sicil

    def ogretmen_bilgileri_goster(self):
        print(f"Adı:{self.ad}\nSoyadı: {self.soyad}\nBransi: {self.brans}\nsicil numarası: {self.sicil_no}")


