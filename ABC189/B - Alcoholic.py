N, X = map(int, input().split())
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    cnt += a * b
    if cnt > X * 100:
        print(i + 1)
        exit()
print(-1)
