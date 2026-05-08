chisla = []

while True:

	chislo = int(input("Введите число: "))

	if chislo != 0:
		chisla.append(chislo)

	else:
		break

chisla.sort()

print(chisla[-1] + chisla[-2], chisla[0] + chisla[1])
