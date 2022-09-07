# NOT COMPLETED
# كنت اسويه فالحصه بس خلصت الحصه
platforms = int(input("Enter the number of platforms: "))
while platforms < 1 or platforms > 300: platforms = int(input("Enter the number of platforms: "))
platform_values = [int(input(f"Enter the {x+1} value of your platform: ")) for x in range(platforms)]
platform_values.sort()
base = platform_values[0]
curr_value = platform_values[0]
poped = platform_values.pop(0)
jumps = 0
for i in platform_values:
    if i > curr_value:
        curr_value = i
    if curr_value <= base+60:
        jumps+=1
print(jumps)
