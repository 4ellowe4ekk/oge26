kolvo = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if 100 <= chislo < 1000:
            if chislo % 4 == 0:
                kolvo += 1

    else:
        break

print(kolvo)