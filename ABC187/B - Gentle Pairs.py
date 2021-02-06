n = int(input())
xy=[list(map(int,input().split())) for _ in range(n)]

ans = 0

for i in range(n-1):
    xi, yi = xy[i]
    for j in range(i + 1, n):
        xj, yj = xy[j]
        a = (yj - yi)/(xj - xi)
        if -1 <= a <= 1:
            ans += 1

print(ans)


