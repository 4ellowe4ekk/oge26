s = 0

for i in range(5):
    chislo = int(input("Введите число: "))
    
    if chislo % 4 == 0:
        if chislo % 10 == 6:
            s += chislo

print(s)
