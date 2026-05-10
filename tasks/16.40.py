n = int(input("Введите колво чисел: "))
kolvo = 0
s = 0

for i in range(n):
    chislo = int(input("Введите число: "))

    if chislo % 7 % 2 == 1:
        kolvo += 1
        s += chislo

if kolvo >= 1:
    print(s / kolvo)

else:
    print("NO")
        