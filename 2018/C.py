numTeams = int(input("Enter the number of teams: "))
teamNames = [input(f"Enter the {x+1} team's names: ") for x in range(numTeams)]

newString = ""
for i in teamNames:
	for n in i:
		if newString.count(n) > 1: continue
		else: newString += n
	print(newString)
	newString = ""
