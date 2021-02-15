h, n = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += a[i]

if h-sum <= 0:
    print("Yes")
else:
    print("No")

# h, n = map(int, input().split())
# s = sum(list(map(int, input().split())))
#
# if h <= s:
#     print("Yes")
# else:
#     print("No")