s = 0
kolvo = 0
itog = 'NO'

while True:
    chislo = int(input("Введите число: "))

    if chislo != 0:
        if 10 <= chislo < 100:

                s += chislo
                kolvo += 1

    else:
        break

if kolvo >= 1:
    print(round(s / kolvo, 1))

else:
    print(itog)