def swap(prize, i, j):
    numArr = [0] * numOfCard
    for k in range(numOfCard-1, -1, -1):
        numArr[k] = prize % 10
        prize //= 10

    numArr[i], numArr[j] = numArr[j], numArr[i]

    prize = 0
    for k in range(numOfCard):
        prize = prize * 10 + numArr[k]

    return prize

def findMax(prize, num, k):
    global ans

    #가지치기
    for i in range(MAXSIZE):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return

    if k == num:
        if prize > ans:
            ans = prize
    else:
        for i in range(numOfCard-1):
            for j in range(i+1, numOfCard):
                findMax(swap(prize, i, j), num, k+1)


MAXSIZE = 720
T = int(input())
for tc in range(T):
    prize, num = map(int, input().split())
    memo = [[0]* MAXSIZE for _ in range(num+1)]
    numOfCard = 0
    ans = 0
    t = prize

    while (t):
        t //= 10
        numOfCard += 1

    findMax(prize, num, 0)
    print("#{} {}".format(tc+1, ans))