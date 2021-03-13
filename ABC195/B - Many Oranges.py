a, b, w = map(int, input().split())
h = w * 1000
if h%a == 0 and h%b == 0:
    print(h//b,h//a)
