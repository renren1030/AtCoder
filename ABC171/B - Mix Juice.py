n, k = map(int, input().split())
food = list(map(int, input().split()))
list = sorted(food)

ans = 0

for i in range(k):
    ans += list[i]

print(ans)

