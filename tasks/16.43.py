s = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if 99 < chislo < 1000:
            if chislo % 4 == 0:
                s += chislo

    else:
        break

print(s)