n, a, b = map(int, input().split())

ans = n // (a + b)
ans *= a

if n % (a + b) != 0:
    ans += min(a, n % (a + b))

print(ans)