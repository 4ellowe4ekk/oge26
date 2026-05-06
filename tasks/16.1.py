n = int(input("Введите колво чисел: "))
maximum = 0

for i in range(n):
    chislo = int(input("Введи число: "))
    
    if chislo % 5 == 0:
        if chislo > maximum:
            maximum = chislo

print(maximum)
