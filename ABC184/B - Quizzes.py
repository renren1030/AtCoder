a, b = map(int,input().split())
s = input()
for i in range(a):
    if s[i] == "x":
        if b != 0:
            b -= 1
        else:
            b = 0
    else:
        b += 1

print(b)