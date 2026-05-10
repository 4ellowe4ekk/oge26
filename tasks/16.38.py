m = 30001

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if chislo % 3 == 0:
            if chislo < m:
                m = chislo

    else:
        break

print(m)