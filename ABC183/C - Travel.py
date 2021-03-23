import itertools

n, k = map(int, input().split())
t = [list(map(int,input().split())) for _ in range(n)]

li = list(range(2,n+1))
p_list = list(itertools.permutations(li))
ans = 0

for i in p_list:
    tra = 0
    tmp_li = i
    num = 1
    for j in tmp_li:
        tra += t[num-1][j-1]
        num = j
    tra += t[num-1][0]
    if tra == k:
        ans += 1

print(ans)