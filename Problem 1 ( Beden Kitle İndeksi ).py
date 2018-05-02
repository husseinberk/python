print("Beden Kitle Endeksi Hesaplama Programı")

kilo = int(input("Lütfen Kilo Değerinizi Giriniz: "))
boy = float(input("Lütfen Boy Değerinizi Giriniz: "))
bki = kilo / ( boy ** 2)

print("Beden Kitle İndeksiniz: {} ".format(bki))

print("Kilo Durumunuz: ")
if (bki <= 18.5):
    print("Zayıf")
elif (bki <= 25):
    print("Normal")
elif (bki <= 30):
    print("Fazla Kilolu")
else:
    print("Obez")

