n = int(input("Введите колво чисел: "))
m = 30001

for i in range(n):
	chislo =  int(input("Введите числа: "))

	if  n <= 1000 and chislo < m and chislo % 3 == 0:
		m = chislo
		
print(m)

