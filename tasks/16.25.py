s = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if chislo % 4 == 0:
            if chislo % 10 == 6:
                s += chislo

    else:
        break

print(s)