n = int(input("Введите колво чисел: "))
max = 0

for i in range(n):
    chislo = int(input("Введи число: "))
    
    if chislo % 5 == 0:
        if chislo > max:
            max = chislo

print(max)
