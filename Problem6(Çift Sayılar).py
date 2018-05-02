liste = []
for i in range(1,101):
    if (i % 2 == 0):
        liste = [i for i in liste]
        liste.append(i)
print(liste)