s = 0
itog = 0

while True:
    chislo = int(input("Введите число: "))
    
    if chislo != 0:
        s += chislo

        if chislo % 2 == 0:
            if chislo % 5 == 0:
                itog += 1

    else:
        break

print(s)
print(itog)