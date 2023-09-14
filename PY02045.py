s = input()
while True:
    if len(s) == 1:
        break
    n = len(s)
    if len(s) % 2 == 1:
        n -= 1
    s1 = s[:n//2]
    s2 = s[n//2:]
    s = str(int(s1) + int(s2))
    print(s)
