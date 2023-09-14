import math
def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
n = int(input())
a = list(map(int, input().split()))
mp = {}
for i in a:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1
for i in a:
    if snt(i):
        if mp[i] != 0:
            print(i, mp[i])
            mp[i] = 0