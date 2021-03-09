n = int(input())
l = []
for i in range(n):
    a,b = list(map(int, input().split()))
    l.append(a)
    l.append(b)

new = set(sorted(l))
new = list(new)
print(max(new[0],new[1]))