n,k = [int(x) for x in input("N, K: ").split(" ")]
heights = [int(x) for x in input("Heights: ").split(" ")]
while len(heights) != n: heights = int(input("Enter Valid heights: "))
heights.sort()
broadbands = []
curr = heights[0]

for i in heights:
	if i >= curr and i <= curr+k: continue
	else: 
		curr = i
		broadbands.append(curr)

broadbands[0] = broadbands[0] -1
print(len(broadbands))
print(" ".join(str(x) for x in broadbands))
