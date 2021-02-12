x = int(input())
n = 100
ans = 0

while n < x:
    n = int(n * 1.01)
    ans += 1

print(ans)