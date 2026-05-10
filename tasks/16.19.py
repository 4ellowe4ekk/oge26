s = 0

while True:
    chislo = int(input("Введите колво: "))

    if chislo != 0:
        if chislo % 7 == 0:
            if chislo % 10 == 2:
                s += chislo

    else:
        break

print(s)