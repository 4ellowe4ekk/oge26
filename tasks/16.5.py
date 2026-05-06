n = int(input("Введите колво чисел: "))
s = 0

for i in range(n):
	chislo = int(input("Введите число: "))
	
	if n <= 1000 and chislo <= 30000 and chislo % 10 == 4:
		s += chislo

print(s)
