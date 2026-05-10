s = 0
kolvo_p = 0
kolvo_n = 0

while True:
    chislo = int(input("Введите число: "))
    
    if chislo != 0:
        s += chislo

        if chislo >= 0:
            kolvo_p += 1

        else:
            kolvo_n += 1

    else:
        break

print(s)
print(kolvo_p - kolvo_n)