T = int(input())
for t in range(T):
    test = list(input())
    res = True
    for i in range(len(test)//2):
        if test[i] == "?" or test[len(test)-i-1] == "?":
            pass
        elif test[i] != test[len(test)-i-1]:
            res = False
    if res:
        print("#{} Exist".format(t+1))
    else:
        print("#{} Not exist".format(t + 1))