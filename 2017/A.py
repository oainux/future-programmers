import sys
unique,holes = "ABDOPQR",0
message = input("Enter your message: ")
if len(message) > 40: sys.exit()
message = message.upper()

for letter in message:
    if letter in unique and letter != "B":holes+=1
    elif letter in unique and letter == "B":holes+=2

print(holes)
