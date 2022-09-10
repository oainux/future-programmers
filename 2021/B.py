n,c = [int(x) for x in input("Enterthe number of servers and the number of orders: ").split(" ")]

# 1 <= n <= c <= 1000
while n < 1 or n > c or c > 1000:n,c = [int(x) for x in input("Enter the number of servers and the number of orders: ").split(" ")]

# times
times = list(map(int,input("Enter the times: ").split(" ")))

# create the servers in a dictinory
dic = {}
for i in range(1,n+1):
	dic[f"{i}"] = 0

# algorithm
for ti in range(len(times)):
	value = []
	for places in dic:
		value.append(dic[places])
	lowValueIndex = value.index(min(value))
	value[lowValueIndex] = value[lowValueIndex] + times[ti]
	times[ti] = lowValueIndex+1
	for i in range(len(dic)):
		dic[f"{i+1}"]=value[i]

# print the result
for i in times:
	print(i, end=" ")
