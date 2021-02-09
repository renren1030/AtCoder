s = input()
t = input()
ls = len(s)
lt = len(t)
ans = lt

for i in range(ls-lt+1):
    num = 0
    for j in range(lt):
        if s[i+j] != t[j]:
            num += 1
    ans = min(ans, num)

print(ans)