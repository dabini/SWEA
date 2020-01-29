T = int(input())

for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    lst = []

    def my_max(a):
        for i in a:
            if i not in lst:
                lst.append(i)
            if i > lst[0]:
                lst[0] = i
        return lst[0]


    def my_min(a):
        for i in a:
            if i not in lst:
                lst.append(i)
            if i < lst[0]:
                lst[0] = i
        return lst[0]

    print('#{0} {1}'.format(t+1, my_max(a)-my_min(a)))