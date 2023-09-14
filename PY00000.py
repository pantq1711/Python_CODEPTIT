import math
a, b, c = list(map(int, input().split()))
if a == 0:
    if b == 0:
        if c != 0:
            print("PT vo nghiem")
        else :
            print("PT vo so nghiem")
    else :
        print(-c/b)
else :
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("PT vo nghiem")
    elif delta == 0:
        x = -b/2/a
        print(x)
    else :
        x1 = (-b + math.sqrt(delta)) / 2 / a
        x2 = (-b - math.sqrt(delta)) / 2 / a
        print(x1 + " " + x2)