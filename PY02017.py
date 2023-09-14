t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    
    count_map = {}
    
    for i in a:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
    
    for i in a:
        if count_map[i] % 2 == 1:
            print(i)
            break
    
    t -= 1
