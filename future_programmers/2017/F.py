sequence = input("Enter your sequence: ")
while " " in sequence or len(sequence) > 40:
    sequence = input("Enter your sequence: ")
if len(sequence) % 2 == 0:
    half = len(sequence) / 2
    if sequence[0:int(half)] == sequence[int(half):]:
        print("Double String")
    else :
        print("Not Double String")
else:
    print("Not Double String")
