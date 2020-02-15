for t in range(1,11):
    t = int(input())
    lst = []
    for _ in range(100):
        lst.append(input())
    res = 0
    for n in range(1,101):
        m = int(n/2)
        for i in range(100):
            for j in range(101-n):
                x=1
                y=1
                for k in range(m):
                    if lst[j+k][i] != lst[j+n-k-1][i]:
                        y=0
                    if lst[i][j+k] != lst[i][j+n-k-1]:
                        x=0
                if x==1 or y==1:
                    res=n
    print("#{} {}".format(t, res))