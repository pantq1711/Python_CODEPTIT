import sys

arr = []
arr1 = []
count = 0

while True:
    s = input().strip()
    if not s:
        break
    count += 1
    end = s[-1]
    if end in ['.', '!', '?']:
        res = s[:-1].lower() + '\n'
        arr.append(res)
        arr1.append(count)
    else:
        res = s.lower() + ' '
        arr.append(res)

for i in range(len(arr)):
    if i == 0 or (i + 1) in arr1:
        print(arr[i].capitalize(), end='')
    else:
        print(arr[i], end='')
