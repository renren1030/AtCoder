a, b = map(int, input().split())
rem = (2 * a + 100) - b
if rem > 0:
    print(rem)
else:
    print("0")
