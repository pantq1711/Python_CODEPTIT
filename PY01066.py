import math
def check(s):
    rev = s[::-1]
    for i in range (1, len(s)):
        if abs(int(s[i]) - int(s[i-1])) != abs(int(rev[i]) - int(rev[i-1])):
            return False
    return True
t = int(input())
while t > 0:
    s1 = input()
    if check(s1):
        print("YES")
    else :
        print("NO")
    t-=1