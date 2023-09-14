n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

count_map = {}

for i in a:
    if i in count_map:
        count_map[i] += 1
    else:
        count_map[i] = 1

max1 = 0
max2 = 0
for i in count_map:
    if count_map[i] > max1:
        max2 = max1
        max1 = count_map[i]
    elif count_map[i] > max2 and max1 != count_map[i]:
        max2 = count_map[i]

if max2 == 0:
    print("NONE")
else:
    min_key = float('inf')
    for i in count_map:
        if count_map[i] == max2 and i < min_key:
            min_key = i
    print(min_key)
