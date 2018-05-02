print("""

Mükemmel Sayı Programı


Çıkmak için "q"ya basınız...


""")

while True:

    sayı = input("Lütfen Sayınızı Giriniz: ")

    if ( sayı == "q"):
        print("Programdan Çıkılıyor...")
        break

    else:
        sonuc = 0
        l = []
        sayı = int(sayı)
        for eleman in range(1,sayı):
            if sayı % eleman == 0:
                    l.append(eleman)

        for m in l:
            sonuc = sonuc+m

        if sonuc == sayı:
            print("Mükemmel Sayı")

        else:
            print("Mükemmel Sayı Değil")

