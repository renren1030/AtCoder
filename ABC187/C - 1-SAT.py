n = int(input())
a = []
b = []

for i in range(n):
    s = input()
    if s[0]=="!":
        b.append(s[1:])
    else:
        a.append(s)

f = list(set(a)&set(b))
if f:
    print(f[0])
else:
    print("satisfiable")