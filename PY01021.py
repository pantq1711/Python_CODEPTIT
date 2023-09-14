t = int(input())
while t > 0:
    s = input()
    sum = 0
    str = ""
    for i in s:
        if i.isdigit():
            sum += int(i)
        else :
            str += i
    print(''.join(sorted(str)), sum, sep = "")
    t-=1