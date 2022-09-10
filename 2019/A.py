n = int(input("Participant: "))
while n < 1 or n > 300: n = int(input("Participant: "))
opinions = [int(x) for x in input("Opinions: ").split(" ")]
while len(opinions) != n: opinions = [int(x) for x in input("Opinions: ").split(" ")]
for i in opinions:
	if i == 1 or i == 0: continue
	else:  opinions = [int(x) for x in input("Opinions: ").split(" ")]

output = None
for i in opinions:
	if i == 1:
		output = "Hard"
		break
	else:
		output = "Easy"
print(output)
