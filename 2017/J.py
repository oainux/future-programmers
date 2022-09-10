n = int(input("Enter: "))
while n < 1: n = int(input("Enter: "))

first=[1,2,3,4,5,0]
second=[3,0,1,2]
third=[4,3,2,1,0,9,8,7,6,5]

for i in range(n):
	first.append(first[0])
	first.pop(0)
	second.append(second[0])
	second.pop(0)
	third.append(third[0])
	third.pop(0)

print(f"{first[0]} {second[0]} {third[0]}")