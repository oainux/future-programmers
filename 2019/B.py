groups = int(input("Groups: "))

# 1 <= groups <= 100
while groups < 1 or groups > 100: groups = int(input("Groups: "))

people_in_groups = [int(x) for x in input("People in each group: ").split(" ")]

# conditionals for people in groups
while len(people_in_groups) != groups: people_in_groups = [int(x) for x in input("People in each group: ").split(" ")]
while max(people_in_groups) != 4: people_in_groups = [int(x) for x in input("People in each group: ").split(" ")]

# algorithm
sum_of_peoples = sum(people_in_groups)
value = 1
taxies = 0
for i in range(sum_of_peoples):
	if value > 4:
		taxies+=1
		value = 1
	value+=1
if value > 0: taxies+=1

# result
print(taxies)
