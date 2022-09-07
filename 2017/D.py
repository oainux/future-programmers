sequence = input("Enter your sequence: ")
limitations = "abcdefgh"

# if sequence values not in limitations make the user input again | if sequence length > 40 make the user input again
k = 0
while k < len(sequence):
	if sequence[k].lower() not in limitations:
		sequence = input("Enter your sequence: ")
	if len(sequence) > 40:
		sequence = input("Enter your sequence: ")
	k+=1

# if entered input is upper make the limitations upper and if entered input is lower make the limitations lower
if sequence.isupper(): limitations = limitations.upper()
else: limitations = limitations.lower()

# neccessary variables for the algorithm
count = 0
currValue = sequence[0]
newString = ""
value = set()

# algorithm
for i in range(len(sequence)):
	if sequence[i] != currValue:
		if count > 2:
			newString+=f"{list(x for x in value)[0]}{count}"
		else:
			for n in range(count):
				newString+=f"{list(x for x in value)[0]}"
		count = 1
		value.clear()
		value.add(sequence[i])
	elif sequence[i] == currValue:
		count += 1
		value.add(sequence[i])
		
	if i == len(sequence) -1:
		if count > 2:
			newString+=f"{list(x for x in value)[0]}{count}"
		else:
			for n in range(count):
				newString+=f"{list(x for x in value)[0]}"
		value.clear()
		
	currValue = sequence[i]

# print the result
print(newString)
