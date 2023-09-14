from itertools import combinations
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
arr = []
for i in a:
    if i not in arr:
        arr.append(i);
arr.sort()
combinations_list = list(combinations(arr, k))
for combo in combinations_list:
    print(*combo)

