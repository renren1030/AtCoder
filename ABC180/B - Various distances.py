import math

n = int(input())
x = list(map(int, input().split()))

m = 0
y = 0
c = 0

for i in x:
    a = abs(i)
    m += a
    y += a**2
    c = max(c, a)

print(m)
print(math.sqrt(y))
print(c)