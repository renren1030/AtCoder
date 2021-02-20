s = input()
n = list(s)
if len(n) >= 2:
    if (s[0::2]).islower() == True and (s[1::2]).isupper() == True:
        print("Yes")
    else:
        print("No")
else:
    if s.islower():
        print("Yes")
    else:
        print("No")
