h, w, x, y = map(int, input().split())
list = [input() for i in range(h)]
ans = 1
if list[x-1][y-2] == ".":
    ans += 1
elif list[x-1][y] == ".":
    ans += 1
elif list[x-2][y-1] == ".":
    ans += 1
elif list[x][y-1] == ".":
    ans += 1

print(ans)