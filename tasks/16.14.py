chisla = []
itog = 0

while True:

    chislo = int(input("Введите число: "))
    chisla.append(chislo)

    if chislo != 0:

        if chislo % 2 == 1 and chislo % 3 == 0:
            itog += 1

    else:
        break

print(len(chisla)- 1)
print(itog)