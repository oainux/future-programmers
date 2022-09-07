rooks = int(input("Enter number of rooks: "))
positions = [int(x) for x in input("Enter positiones: ").split(" ")]
while len(positions) != rooks*2:
	positions = [int(x) for x in input("Enter positiones: ").split(" ")]

x = [positions[x] for x in range(0,len(positions),+2)]
y = [positions[x] for x in range(1,len(positions),+2)]

value = (None, None)
isSafe = True
for i in zip(x,y):
	if i[1] == value[1]:
		isSafe = False
		break
	value = i

print("Not Safe") if not isSafe else print("Safe")
