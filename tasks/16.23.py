s = 0

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if chislo % 4 == 0:
            if chislo % 10 == 8:
               if chislo <= 300:
                   s += chislo 

    else:
        break

print(s)