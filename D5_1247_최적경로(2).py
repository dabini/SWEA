def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc():
    global ans
    dist = 0
    for i in range(N-1):
        dist += getD(customer[t[i]], customer[t[i+1]])
    dist += getD(company, customer[t[0]])
    dist += getD(customer[t[N-1]], home)

    if ans > dist:
        ans = dist

def perm(n, k):
    if k == n:
        calc()
    else:
        for i in range(n):
            if visited[i]:
                continue
            t[k] = i
            visited[i] = 1
            perm(n, k+1)
            visited[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    visited = [0] * N
    t = [0]* N
    ans = 0x7fffffff

    company = (temp[0], temp[1])
    home = (temp[2], temp[3])
    customer = []

    for i in range(4, len(temp), 2):
        customer.append((temp[i], temp[i+1]))

    perm(N, 0)
    print("#{} {}".format(tc+1, ans))
