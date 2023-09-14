n = input()
m = len(n)
if m % 2 == 1:
    m -= 1
mp = {}
for i in range(int(m/2)):
    tmp = int(n[0]) * 10 + int(n[1])
    if tmp in mp:
        mp[tmp]+=1
    else :
        mp[tmp] = 1
    n = n[2::]
for i in sorted(mp):
    print(i, end = ' ')