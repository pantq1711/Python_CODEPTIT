import math

t = int(input())
while t > 0:
    m = {}
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    res = 1e9
    val = 0
    for i in m:
        if m[i] > val:
            val = m[i]
            res = i
        if m[i] == val:
            res = min(res, i)
    print(res)
    t -= 1
