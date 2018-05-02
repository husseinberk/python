toplam = 0

while True:
    sayı = input("Lütfen bir sayı giriniz...")
    if (sayı == "q"):
        break
    sayı = int(sayı)

    toplam += sayı


print("Girdiğiniz sayıların toplamı: ",toplam)
