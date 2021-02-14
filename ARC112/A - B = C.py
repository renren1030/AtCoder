# n = int(input())
# ans = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     list = list(range(a, b+1))
#     for j in range(len(list)):
#         for k in range(len(list)):
#             c = list[j] - list[k]
#             if c in list:
#                 ans += 1
#
# print(ans)
import sys

readline = sys.stdin.buffer.readline


def solve():
    l, r = map(int, readline().split())
    n = r - l * 2
    if n < 0:
        print(0)
        return
    print((n + 1) * (n + 2) // 2)


t = int(readline())
for _ in range(t):
    solve()