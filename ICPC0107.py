t = int(input())
def convert(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)
while t > 0:
    [p, q] = input().split()
    s = input().split()
    if len(s) > 1:
        a = s[0]
        b = s[1]
    else:
        a = s[0]
        b = input()
    x = convert(a, b, p, q)
    y = convert(a, b, q, p)
    print(min(x, y), max(x, y))
    t-=1