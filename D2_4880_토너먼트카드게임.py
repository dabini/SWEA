def rsp(a, b): #1 가위 2 바위 3 보
    if lst[a] == lst[b]:
        return a
    else:
        if lst[a] == 1:
            if lst[b] == 2:
                return b
            elif lst[b] == 3:
                return a
        elif lst[a] == 2:
            if lst[b] == 1:
                return a
            elif lst[b] == 3:
                return b
        else:
            if lst[b] == 1:
                return b
            elif lst[b] == 2:
                return a

def Find(low, high):

    if low == high:
        return low

    else:
        a= Find(low, (low + high) // 2)
        b= Find((low + high) // 2+1, high)

    return rsp(a, b)

T = int(input())
for t in range(T):
    num = int(input())
    lst = [0]
    lst += list(map(int, input().split()))

    print("#{} {}".format(t+1, Find(1, num)))