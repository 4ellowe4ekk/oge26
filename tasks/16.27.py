n = int(input("Введите колво чисел: "))
kolvo = 0

for i in range(n):
    chislo = int(input("Введите число: "))

    if chislo % 6 == 0:
        if chislo % 10 == 4:
            kolvo += 1

print(kolvo)