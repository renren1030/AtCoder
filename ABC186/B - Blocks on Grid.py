H, W = map(int, input().split())
mi = 100
g = 0
for i in range(H):
    a = list(map(int, input().split()))
    mi = min(mi, min(a))
    g += sum(a)

print(g - H*W*mi)