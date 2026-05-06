n = int(input("Ввелите колво чисел: "))
kolvo = 0

for i in range(n):
	chislo = int(input("Введите число: "))

	if n <= 1000 and chislo <= 30000 and chislo % 4 == 0:
		kolvo += 1

print(kolvo)
