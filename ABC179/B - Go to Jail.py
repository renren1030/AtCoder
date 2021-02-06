n = int(input())
ans = 0
cnt = 0

list = [list(map(int, input().split())) for i in range(n)]


for i in range(n):
    a, b = list[i]
    if a == b:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

if ans >= 3:
    print("Yes")
else:
    print("No")