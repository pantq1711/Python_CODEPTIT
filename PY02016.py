t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    mp = {}
    for i in a:
        if i in mp:
            mp[i] += 1
        else :
            mp[i] = 1
    max = mp[a[0]]
    for i in mp:
        if mp[i] > max:
            max = mp[i]
            res = i
        if mp[i] == max:
            res = i
    if max <= n/2:
        print("NO")
    else :
        print(res)
    t-=1