import math
def check(n):
    # tmp = n[::-1]
    # if tmp == n :
    #     return True
    # return False
    return n[::-1] == n
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    for i in range(n):
        x = str(i)
        tmp = x[::-1]
        if snt(i) and snt(int(tmp)) and check(str(i)) == False and int(tmp) < n and int(tmp) > i:
            print(x,tmp,end = ' ')
    print()
    t-=1
# 13  31
# 13  31  17  71  37 73 79  97
# 13  31  
# 13  31  17  71  37  73  79  97