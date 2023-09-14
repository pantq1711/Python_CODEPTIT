t = int(input())
def is_valid_ipv4(s):
    a = s.split(".")
    if len(a) != 4:
        return "NO"
    for i in a:
        try:
            num = int(i)
            if num < 0 or num > 255:
                return "NO"
        except ValueError:
            return "NO"
    return "YES"
while t > 0:
    s = input()
    print(is_valid_ipv4(s))
    t -= 1