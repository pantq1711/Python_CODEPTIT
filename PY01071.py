s = input()
if len(s) < 3:
    print("no")
else :
    tmp = s.lower()[-3::]
    if tmp == ".py":
        print("yes")
    else :
        print("no")