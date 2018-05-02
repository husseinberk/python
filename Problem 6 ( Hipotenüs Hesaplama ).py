print("Hipotenüs Hesaplama Formülü")

a = int(input("Lütfen Üçgenin Kısa Kenar Uzunluğunu Girin: "))
b = int(input("Lütfen Üçgenin Uzun Kenar Uzunluğunu Girin: "))

print(str("Üçgenin Hipotenüs Formülü: a^2 + b^2 = c^2"))

print("Buna Göre...")

c = print("Üçgenin hipotenüsü {}'nın karesi + {}'nin karesi".format(a,b))

print("Elde ettiğimiz sonucun kare kökünü alıyoruz")

d = (a ** 2) + (b ** 2)
e = int(d ** 0.5)

print("Üçgenimizin Hipotenüs'ü: {}√2 = {}'dir. ".format(d,e))
