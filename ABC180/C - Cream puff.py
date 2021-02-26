import math

n = int(input())
ans = []

for i in range(1,math.floor(math.sqrt(n))+1):
    if n%i == 0:
        ans.append(i)
        ans.append(n//i)

l = sorted(set(ans))

for i in l:
    print(i)