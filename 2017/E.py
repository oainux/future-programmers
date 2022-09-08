platforms = int(input("Enter the number of platforms: "))

# make the user input again if platforms are less than 1 or greater than 300
while platforms < 1 or platforms > 300: platforms = int(input("Enter the number of platforms: "))

# input the values of the platform
platform_values = [int(input(f"Enter the {x+1} value of your platform: ")) for x in range(platforms)]

# neccessary stuff for the algorithm
platform_values.sort()
base = platform_values[0]
curr = platform_values[0]
jumps = 0

#algorithm
for i in platform_values:
	if i > curr and i <= base+60:
		curr = i
	else:
		jumps+=1
		base = curr
print(jumps)