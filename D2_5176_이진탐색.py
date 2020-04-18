"""
트리를 만들기
6이면 1 아래 2, 3/ 2 아래 45 3 아래 67 .. 4 아래 89 5 아래 10 11 6아래 12 13 7 아래 14 15
수 넣기(중위 순회로)
"""
def inOrder(n):
    if n <= num:
        if tree[n]:
            inOrder(tree[n][0])
            res.append(n)
            inOrder(tree[n][1])
        if n not in res:
            res.append(n)

T = int(input())
for t in range(T):
    num = int(input())
    tree = [[] for _ in range(num*2)]
    res = [0]

    for i in range(1, num+1):
        if 2*i <= num:
            tree[i].append(2*i)
            tree[i].append(2*i+1)
    # print(tree)
    inOrder(1)
    # print(res)
    print("#{} {} {}".format(t+1, res.index(1), res.index(num//2)))