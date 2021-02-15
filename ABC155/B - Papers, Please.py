# n = int(input())
# a = list(map(int, input().split()))
# b = []
# ans = 0
#
# for i in range(n):
#     if a[i] % 2 == 0:
#         b.append(a[i])
#     else:
#         continue
#
# for i in range(len(b)):
#     if b[i] % 3 == 0 or b[i] % 5 == 0:
#         ans += 1
#     else:
#         continue
#
# if ans == len(b):
#     print("APPROVED")
# else:
#     print("DENIED")

i = int(input())
if i % 3 and i % 5:
    print("DENIED")
else:
    print("OK")