n = int(input("Введите колво чисел: "))
chisla = []
kolvo = 0

for i in range(n):
	v = int(input("Введите число: "))
	chisla.append(v)

	if 1 <= n <= 30:
		if 1 <= v <= 300:
			if v <= 30:
				kolvo += 1

chisla.sort()

print(chisla[-1] - chisla[0])
print(kolvo)
