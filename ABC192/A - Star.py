n = int(input())
while True:
    if n >= 100:
        n = n - 100
    else:
        n = 100 - n
        break

print(n)
