n, m = map(int, input().split())
l = []
a = 0

for i in range(n):
    s = input()
    l.append(s)

ans = l[0].count("0")

for i in range(n):
    if ans != l[i].count("0"):
        a += 1

print(a)


