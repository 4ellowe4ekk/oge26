n = int(input("Введите колво чисел: "))
m = 30001

for i in range(n):
	chislo = int(input("Введите число: "))

	if n <= 1000 and chislo % 10 == 6:
		if chislo < m:
			m = chislo

print(m)
