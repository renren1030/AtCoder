n = int(input())
s = input()

for i in s:
    m = (ord(i) - ord('A') + n) % 26
    ans += chr(m + ord('A'))

print(ans)