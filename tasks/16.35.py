kolvo = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if chislo % 4 == 0:
            if chislo % 10 == 2:
                kolvo += 1

    else:
        break

print(kolvo)