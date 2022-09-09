leaves = int(input("Enter the number of leaves: "))
frogs = int(input("Enter the number of frogs: "))
jumps = [int(x) for x in input("Enter the jump radius for each frog: ").split(" ")]
snails = leaves * 10


# make each frog take its value from the jumps
sequence = {}
for i in range(frogs):
	sequence[f"frog_{i+1}"] = jumps[i]

# make the jump
for i in sequence:
	for n in range(1,leaves,sequence[i]):
		snails -= 1

print(snails)