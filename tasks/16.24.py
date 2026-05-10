n = int(input("Введите колво чисел: "))
m = 30001

for i in range(n):
    chislo = int(input("Введите число: "))
    
    if chislo % 2 == 0:
        if chislo < m:
            m = chislo

print(m)