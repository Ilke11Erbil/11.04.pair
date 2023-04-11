from ogretmen import Ogretmen
from ogrenci import Ogrenci

ogrenciList = []
ogretmenList = []

def ogrenci_ekle():
    ad = input("Öğrenci adı:")
    soyad = input("Öğrenci soyadı:")
    okul_numarası = input("Öğrenci okul numarası:")
    sinif = input("Öğrenci sinif:")

    yeniOgrenci = Ogrenci(ad, soyad, okul_numarası, sinif)
    ogrenciList.append(yeniOgrenci)

def ogretmen_ekle():
    ad = input("Öğretmen Adı:")
    soyad = input("Öğretmen Soyadı")
    brans = input("Öğretmen Branşı:")
    sicil_no = input("Öğretmen Sicil No:")

    yeniOgretmen = Ogretmen(ad, soyad, brans, sicil_no)
    ogretmenList.append(yeniOgretmen)

def kayitlariGoster():
    print("Öğrenciler:")
    for ogrenci in ogrenciList:
        ogrenci.ogrenci_bilgileri_goster()

    print("\nÖğretmenler:")
    for ogretmen in ogretmenList:
        ogretmen.ogretmen_bilgileri_goster()
while True:
     print
     
   





