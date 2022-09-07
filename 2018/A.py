import sys
n = int(input("Enter the length of your sequence: "))

start = list(int(x) for x in input("Enter the four nums of start for your sequence: ").split(" "))

if n <= 4: 
	print(0)
	sys.exit()
	
for i in start:
	if i % 2 == 0: 
		print(0)
		sys.exit()

k = 0
while k<n-4:
	acc = 0
	for i in range(k,k+4):
		if start[i] % 2 == 0: continue
		else: acc += start[i]
	start.append(acc)
	k+=1

print(" ".join(map(str,start)))
