kolvo = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if 1 <= chislo < 10:
            if chislo % 3 == 0:
                kolvo += 1

    else:
        break

print(kolvo)