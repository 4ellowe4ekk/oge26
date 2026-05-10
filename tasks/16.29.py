s = 0
kolvo = 0
itog = 'NO'

while True:
    chislo = int(input("Введите число: "))
    
    if chislo != 0:
        if chislo % 8 == 0:

            s += chislo
            kolvo += 1

    else:
        break

if kolvo == 0:
    print(itog)

else:
    print(round(s / kolvo, 1))