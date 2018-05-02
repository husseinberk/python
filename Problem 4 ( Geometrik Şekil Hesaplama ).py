print("Geometrik Şekil Hesaplama İşlemi")


şekil = str(input("Lütfen Hangi Geometrik Şekli Girmek İstediğinizi (Üçgen-Dörtgen) Seçiniz:"))

if (şekil == "Dörtgen"):
    print("Lütfen kenarları giriniz: ")
    a = int(input("Dörgen'in ilk kenar uzunluğunu yazın: "))
    b = int(input("Dörtgen'in ikinci kenar uzunluğunu yazın: "))
    c = int(input("Dörgen'in üçüncü kenar uzunluğunu yazın: "))
    d = int(input("Dörgen'in dördüncü kenar uzunluğunu yazın: "))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif (şekil == "Üçgen"):
    a = int(input("1. Kenar: "))
    b = int(input("2. Kenar: "))
    c = int(input("3. Kenar: "))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

else:
    print("Geçersiz Şekil...")