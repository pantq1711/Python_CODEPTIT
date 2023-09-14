mp = {}
a = []
while len(a) < 10:
    a += list(map(int, input().split()))

for i in a:
    if i % 42 not in mp:
        mp[i % 42] = 1
print(len(mp))