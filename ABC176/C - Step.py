n = int(input())
a = list(map(int, input().split()))
t = 0
ans = 0

for i in range(n):
    if t > a[i]:
        ans += t - a[i]
    else:
        t = a[i]

print(ans)