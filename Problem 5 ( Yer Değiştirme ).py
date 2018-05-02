print("Girilen Sayıların Yerlerini Değiştirme")


a = int(input("Lütfen 'Birinci' Sayıyı Giriniz: "))
b = int(input("Lütfen 'İkinci' Sayıyı Giriniz: "))

print("Girilen Değerler:\nA Değeri: {}\nB Değeri: {}".format(a,b))

a,b=b,a

print("Yer Değiştirilmiş Hali İle Değerler:\nA Değeri: {}\nB Değeri: {}".format(a,b))