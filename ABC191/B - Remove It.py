n, x = map(int, input().split())
num = list(map(int, input().split()))

list = []
for i in range(n):
    d = num[i]
    if d not in list:
        list.append(d)
        if x in list:
            list.remove(x)

# result = sorted(set(num), key=num.index)
# result.remove(x)

for i in list:
    print("{} ".format(i), end="")

