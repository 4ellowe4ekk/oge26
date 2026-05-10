n = int(input("Введите колво: "))
itog = 'NO'
kolvo = 0

for i in range(n):
    chislo = int(input("Введите число: "))
    
    if chislo == 10:
        itog = 'YES'

    elif chislo < 5:
        kolvo += 1
    
print(kolvo)
print(itog)