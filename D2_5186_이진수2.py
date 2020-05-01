def convert(num):
    global tmp
    k = 1
    tmp = ''
    while num:
        if len(tmp) >=13:
            tmp = 'overflow'
            break
        if num >= (0.5)**k:
            num -= (0.5)**k
            tmp += '1'
        else:
            tmp += '0'
        k += 1

T = int(input())
for t in range(T):
    num = float(input())
    # print(num)
    convert(num)
    print("#{} {}".format(t+1, tmp))