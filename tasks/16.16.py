dlina = 0
s = 0

while True:
    chislo = int(input("Введите число: "))
    
    if chislo != 0:
        dlina += 1

        if chislo % 2 == 0:
            s += chislo

    else:
        break

print(dlina)
print(s)