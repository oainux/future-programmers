customors = int(input("Enter the amount of customers: "))

# make sure the n is always greater than or equal to 1 and less than and equal to 10**5
while customors < 1 or customors > pow(10,5):
    customors = int(input("Enter the amount of customers: "))

times = [int(x) for x in input("Enter a time for each customer's order: ").split(" ")]

# if len(times) less than customers make the user input the time again
if len(times) != customors:
    times = [int(x) for x in input("Enter a time for each customer's order: ").split(" ")]

# make sure each time is greater than or equal to 1 and less than or equal to 10**9
k = 0
while k < len(times):
    if times[k] < 1 or times[k] > pow(10,9):
        times = [int(x) for x in input("Enter a time for each customer's order: ").split(" ")]
    k+=1

times.sort()

satisfied = 0

# algorithm
for i in range(len(times)):
    if i == 0: satisfied+=1
    else:
        if sum(times[:i]) <= times[i]:
            satisfied+=1
print(satisfied)
