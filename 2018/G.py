import sys
n = int(input("Enter: "))
if n == 0: sys.exit()
while n < 1 or n > 999999: n = int(input("Enter: "))
amount = 0
for i in range(n):
	value = f"{i}"
	if "4" in value: amount +=1
print(n-amount)