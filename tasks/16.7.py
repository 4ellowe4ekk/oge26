n = int(input("Введите колво чисел: "))
m = 0

for i in range(n):
        chislo = int(input("Введите число: "))

        if n <= 1000 and chislo <= 30000 and chislo % 10 == 3:
                if chislo > m:
                        m = chislo

print(m)
