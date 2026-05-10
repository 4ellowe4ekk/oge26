kolvo = 0

for i in range(8):
    chislo = int(input("Введите число: "))

    if chislo % 3 == 0:
        if chislo % 10 == 4:
            kolvo += 1

print(kolvo)