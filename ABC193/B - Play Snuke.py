n = int(input())
h = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a < c:
        h.append(b)
    else:
        continue

new = sorted(h)
if new:
    print(new[0])
else:
    print("-1")