n = int(input("Введите колво дней: "))
kolvo = 0
s = 0

for i in range(n):
    chislo = int(input("Введите число: "))

    if chislo > 0:
        s += chislo
        kolvo += 1

print(s / kolvo)
print(kolvo)