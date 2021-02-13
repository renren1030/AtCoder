n, k = map(int, input().split())
a = []

for i in range(k):
    d = int(input())
    ai = list(map(int, input().split()))
    a = a + ai

print(n-len(set(a)))