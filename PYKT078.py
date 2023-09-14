t = int(input())
while t > 0:
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a1 = []
    a2 = []
    Max = max(a)
    for i in range(n):
        if a[i] == Max:
            a.insert(i, m)
            break;
    for i in a:
        if i < 0:
            a1.append(i)
        else :
            a2.append(i)
    for i in a1:
        print(i, end = ' ')
    for i in a2:
        print(i, end = ' ')
    print()
    t -= 1