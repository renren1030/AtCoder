n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
ans = (m * n) - sum_a

if ans > k:
    ans = -1
elif ans < 0:
    ans = 0

print(ans)