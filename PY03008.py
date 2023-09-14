n = int(input())
t = n - 1
mp = {}
for i in range(t):
    x, y = list(map(int, input().split()))
    if y not in mp:
        mp[y] = 1
    else :
        mp[y] += 1
    if x not in mp:
        mp[x] = 1
    else :
        mp[x] += 1
ok = 0
for i in range(1, n + 1):
    if not(i in mp) or mp[i]  == 0:
        ok = 1
if ok == 0:
    print("Yes")
else :
    print("No")