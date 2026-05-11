n = int(input("Введите колво чисел: "))
s = 0

for i in range(n):
    chislo = int(input("Введите число: "))

    if chislo % 7 % 10 == 1:
        s += chislo

print(s)