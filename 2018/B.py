import sys
l,d,s = list(int(x) for x in input("Enter the range, num of steps forward, num of steps backward: ").split(" "))
while s > d or d > l: l,d,s = list(int(x) for x in input("Enter the range, num of steps forward, num of steps backward: ").split(" "))
if l == 0 and d == 0 and s == 0: sys.exit()
k = 0
days=0
while k < l:
    k+=d
    days+=1
    if k == l: break
    k -= s
print(days)