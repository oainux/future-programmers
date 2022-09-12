n, q = [int(x) for x in input("Enter N and Q: ").split(" ")]

# conditions for N and Q
while n < 1 or n > 5000: n = int(input("Enter valid N: "))
while q < 1 or q > pow(10,6): n = int(input("Enter valid Q: "))

# operations and values and their condition
d_o = [int(x) for x in input("Devices and Operations: ").split(" ")]
while len(d_o) != q*2: d_o = [int(x) for x in input("Devices and Operations: ").split(" ")]

# declare the nesseccary variables
operations = [d_o[x] for x in range(0,(q*2),2)]
values = [d_o[x] for x in range(1,(q*2),2)]
untested = [x+1 for x in range(n)]
tested = []
scrap = []

# algorithm
i = 0
li = list(zip(operations,values))
while i < len(li):
	if li[i][0] == 1:
		tested.append(li[i][1])
		untested.remove(li[i][1])
	elif li[i][0] == 2:
		scrap.append(li[i][1])
		tested.remove(li[i][1])
	elif li[i][0] == 3:
		scrap.append(li[i][1])
		untested.remove(li[i][1])
	elif li[i][0] == 4:
		tested.append(li[i][1])
		scrap.remove(li[i][1])
	i+=1

# result
print("Untested: ",end=" ")
for i in untested: print(i,end=" ")
print()
print("Tested: ", end=" ")
for i in tested: print(i,end=" ")
print()
print("Scrap: ", end=" ")
for i in scrap: print(i,end=" ")