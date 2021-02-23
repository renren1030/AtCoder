n, k = map(int, input().split())
height = list(map(int, input().split()))
ans = 0

for i in range(n):
    if height[i] >= k:
        ans += 1
    else:
        continue

print(ans)