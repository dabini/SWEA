T = int(input())
for t in range(T):
    N = int(input())
    check = [0] * 201
    for n in range(N):
        now, goal = map(int, input().split())
        if now < goal:
            for a in range((now+1)//2, (goal+1)//2+1):
                check[a] +=1
        else:
            for a in range((goal+1)//2, (now+1)//2+1):
                check[a] +=1
    res = 0
    for i in range(201):
        if check[i] > res:
            res = check[i]
    print("#{} {}".format(t+1, res))