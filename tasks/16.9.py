s = 0

while True:

	chislo = int(input("Введите число: "))
	
	if chislo <= 30000 and chislo != 0 and chislo % 10 == 4 and chislo % 6 == 0:
		s+= chislo
	
	if chislo == 0:
		break

print(s)
