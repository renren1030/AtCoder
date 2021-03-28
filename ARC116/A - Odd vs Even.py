def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

t = int(input())
even = 0
odd = 0
for i in range(t):
    n = int(input())
    ans = divisor(n)
    for i in range(len(ans)):
        if ans[i] % 2 == 0:
            even += 1
        else:
            odd += 1
            if even == odd:
                print("Same")
            elif even > odd:
                print("Even")
            else:
                print("Odd")




