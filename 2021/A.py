n = int(input("Enter the amount of houses on one side: "))

while n > pow(10,5):n = int(input("Enter the amount of houses on one side: "))

house = int(input("Enter the house you want to find the number of: "))

even = []
odd = []
for i in (n+1 for n in range(n*2)):
	if i % 2 == 0: even.append(i)
	else: odd.append(i)
odd = odd[::-1]
if house in even:
	print(odd[even.index(house)])
elif house in odd:
	print(even[odd.index(house)])
