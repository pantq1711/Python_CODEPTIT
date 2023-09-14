t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print((a[n-1] - a[0] - len(set(a)) + 1))
    t-=1