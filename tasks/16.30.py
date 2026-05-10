s = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if 10 <= chislo < 100:
            if chislo % 8 == 0:
                s += chislo

    else:
        break

print(s)