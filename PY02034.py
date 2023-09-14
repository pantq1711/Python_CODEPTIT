n = input()
mp = {}
len = len(n)
if len % 2 == 1:
    len -= 1
for i in range(len):
    if i % 2 == 0:
        x = int(n[i : i + 2])
        if x in mp:
            mp[x] += 1
        else :
            mp[x] = 1
for i in mp:
    if mp[i] != 0:
        print(i, mp[i])
        mp[i] = 0