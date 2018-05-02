number = int(input("Sayı giriniz:"))
numberstr = str(number)
total = 0

for i in numberstr:
    print(i)
    digit = int(i) ** len(numberstr)
    print(digit)
    total += digit
    print(total)

if (total == number):
    print(number, "bir armstrong sayısıdır.")

else:
    print(number, "bir armstrong sayısı değildir.")