kolvo = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if chislo % 5 == 0 or chislo % 9 == 0:
            kolvo += 1

    else:
        break

print(kolvo)