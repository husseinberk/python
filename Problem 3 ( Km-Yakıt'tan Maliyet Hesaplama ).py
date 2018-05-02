print("Yakıt-Km Maliyet Hesaplama Programı")

a = int(input("Kaç Kilometre Yol Gidileceğini Girin:"))
b = float(input("Aracın '1' Kilometrede Ne kadar Yakıt Tükettiğini Yazın (Kuruş):"))
c = a*b

print("Aracınızın Bu Yolculuktaki Toplam Yakıt Maliyeti {}₺'dir".format(c))