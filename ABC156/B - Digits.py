n, k = map(int, input().split())
ans = 0

while n > 0:
    n = n // k
    print(n)

