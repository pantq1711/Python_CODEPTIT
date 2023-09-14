n = int(input())
a = list(map(int, input().split()))
check = False
b = sorted(a)
for i in range(0, 30001):
    if not((i+1) in b):
        check = True
        print(i + 1)
        break;
if check == False:
    print(n + 1)
