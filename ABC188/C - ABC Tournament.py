import collections

n = int(input())
a = list(map(int, input().split()))

q = collections.deque(a)

while len(q)>2:
    k = q.popleft()
    l = q.popleft()
    q.append(max(k,l))

mn = min(q)
print(a.index(mn)+1)