n = int(input("Введите колво учатсников: "))
itog = 'NO'
m = 0

for i in range(n):
    chislo = int(input("Введите число: "))

    if chislo > m:
        m = chislo

    if chislo == 0:
        itog = 'YES'

print(m)
print(itog)