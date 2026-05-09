n = int(input("Введите колво: "))
itog = 'NO'
m = 0

for i in range(n):
	s = int(input("Введите скорость: "))

	if 1 < n < 30:
		if 1 < s < 300:
			if s < 30:
				itog = 'YES'	

	if s > m:
		m = s


print(m)
print(itog)
