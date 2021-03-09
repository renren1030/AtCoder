n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(len(l)):
    for j in range(1, len(l)-1):
        ans += (l[i]-l[j])**2
        print(l[i],l[j],ans)

print(ans)
