hour = int(input())
min = int(input())

res = (hour*60)-(min*11)
res2 = res/2

if hour < 6:
	result = res2
elif hour > 6:
	result = 360-res2
print(abs(result))
