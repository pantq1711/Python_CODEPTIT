import functools
def cmp(a, b):
    if tcs(a) == tcs(b):
        if a > b:
            return 1
        else :
            return -1
    else :
        if tcs(a) > tcs(b):
            return 1
        else :
            return -1
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, key = functools.cmp_to_key(cmp))
    for i in a : print(i, end = " ")
    print()
    t -= 1