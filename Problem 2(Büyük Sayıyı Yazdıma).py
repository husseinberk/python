
a = int(input("Lütfen Birinci Sayı Giriniz: "))
b = int(input("Lütfen İkinci Sayıyı Giriniz: "))
c = int(input("Lütfen Üçüncü Sayıyı Giriniz: "))

print ("Girdiğiniz En Büyük Sayı: ")

if (a>b) and (a>c):
    print (a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)

print("#Son#")