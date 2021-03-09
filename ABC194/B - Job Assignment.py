# n = int(input())
# l = []
# for i in range(n):
#     a,b = list(map(int, input().split()))
#     l.append(a)
#     l.append(b)
#
# new = set(sorted(l))
# new = list(new)
# print(max(new[0],new[1]))
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n) :
	a[i], b[i] = map(int, input().split())
res = 1000000000
for i in range(n) :
	for j in range(n) :
		res = min(res, a[i] + b[j] if i == j else max(a[i], b[j]))
print(res)