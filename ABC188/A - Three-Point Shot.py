X, Y = map(int, input().split())
if X > Y:
    if X < Y + 3:
        print("Yes")
    else:
        print("No")
else:
    if X + 3 > Y:
        print("Yes")
    else:
        print("No")
