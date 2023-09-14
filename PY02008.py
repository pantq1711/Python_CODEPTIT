import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n, x = list(map(int, input().split()))
Prime = []
for i in range (2, 10000):
    if snt(i):
        Prime.append(i)
print(x, end = ' ')
for i in range(0, n):
    x += Prime[i]
    print(x, end = ' ')