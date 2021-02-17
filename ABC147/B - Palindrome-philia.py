s = input()

s = input()
s_len = len(s)
ans = 0

for i in range(s_len // 2):
    if s[i] != s[s_len - 1 - i]:
        ans += 1

print(ans)