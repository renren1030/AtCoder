import math
l = int(input())

ans = math.factorial(l-1) // (math.factorial(l-12) * math.factorial(11))
print(ans)