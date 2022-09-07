import sys
word = str(input("Enter your word: "))
for x in word:
	if x == " " or len(word) > 40: sys.exit()
	
i=0
while i <= len(word):
	for j in range(0,i+1):
		if len(word) == 0: break
		else:
			print(word[0],end=" ")
			word = word.replace(word[0],"",1)
	print()
	i+=1

for i in range(len(word)): print(word[i],end=" ")

