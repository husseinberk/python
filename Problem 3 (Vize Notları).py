
Vize1 = float(input("Lütfen Vize 1 Notunuzu Giriniz: "))
Vize2 = float(input("Lütfen Vize 2 Notunuzu Giriniz: "))
Final = float(input("Lütfen Final Notunuzu Giriniz: "))

Toplam_Not = ((Vize1 * 0.3) + (Vize2 * 0.3) + (Final * 0.4))


print("Yıl Sonu Notunuz: {}".format(Toplam_Not))


print("Harf Notunuz:\n")
if(Toplam_Not >=90):
    print("AA")
elif(Toplam_Not >=85):
    print("BA")
elif(Toplam_Not >=80):
    print("BB")
elif(Toplam_Not >=75):
    print("CB")
elif(Toplam_Not >=70):
    print("CC")
elif(Toplam_Not >=65):
    print("DC")
elif(Toplam_Not >=60):
    print("DD")
elif(Toplam_Not >=55):
    print("FD")
else:
    print("FF")
