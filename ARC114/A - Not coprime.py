n = int(input())
A = list(map(int, input().split()))
B = []
ans = 1

for i in range(n):
    if A[i] % 2 == 0:
        B.append(2)
    elif A[i] % 3 == 0:
        B.append(3)
    elif A[i] % 5 == 0:
        B.append(5)
    elif A[i] % 7 == 0:
        B.append(7)
    else:
        B.append(A[i])

C = list(set(B))

for i in range(len(C)):
    ans *= C[i]

print(ans)



