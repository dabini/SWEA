from collections import deque

def bfs():
    global res
    while q:
        now, cnt = q.popleft()
        if now == M:
            res = cnt
            return

        for i in range(4):
            tmp = 0
            if i == 0:
                tmp = now + 1
                if 0< tmp <= 1000000 and check[tmp] != t+1:
                    q.append((tmp, cnt+1))
                    check[tmp] = t+1
            elif i == 1:
                tmp = now - 1
                if 0< tmp <= 1000000 and check[tmp] != t+1:
                    q.append((tmp, cnt+1))
                    check[tmp] = t+1
            elif i == 2:
                tmp = now * 2
                if 0< tmp <= 1000000 and check[tmp] != t+1:
                    q.append((tmp, cnt+1))
                    check[tmp] = t+1
            else:
                tmp = now - 10
                if 0< tmp <= 1000000 and check[tmp] != t+1:
                    q.append((tmp, cnt+1))
                    check[tmp] = t+1

T = int(input())
check = [0]* 1000001
for t in range(T):
    N, M = map(int, input().split())
    q = deque()
    q.append((N, 0))
    res = 0
    check[N] = t+1
    bfs()
    print("#{} {}".format(t+1, res))