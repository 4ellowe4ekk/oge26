n = int(input("Введите колво: "))
kolvo = 0
s = 0

for i in range(n):
	v = int(input("Введите скорость: "))

	if 1 < n < 30:
		if 1 < v < 300:
			if v <= 40:
				kolvo += 1

	s += v

print(round(s / n, 1))

if kolvo >= 2:
	print('YES')
else:
	print('NO')
