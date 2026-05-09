n = int(input("Введите колво: "))
itog = 'NO'
m = 0

for i in range(n):
	v = int(input("Введите скорость: "))

	if 1 < n < 30:
		if 1 < v < 300:
			if v < 30:
				itog = 'YES'	

	if v > m:
		m = v


print(m)
print(itog)
