n = int(input("Введите колво чисел: "))
s = 0

for i in range(n):
	chislo = int(input("Введите число: "))

	if n <= 100 and chislo <= 300 and chislo % 6 == 0:
		s += chislo

print(s) 
