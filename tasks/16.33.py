a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
kolvo = 0

for i in range(a, b + 1):

    if i % 2 == 0:
        kolvo += 1
    

print(kolvo)