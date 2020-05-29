def find(node, lst):
    while node > 1:
        for t in tree:
            if node in t:
                lst.append(tree.index(t))
                node = tree.index(t)
                break

def subtree(node):
    global cnt
    if tree[node]:
        cnt += len(tree[node])
        for n in tree[node]:
            subtree(n)

T = int(input())
for t in range(T):
    V, E, nodeA, nodeB = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]
    for i in range(0, len(nodes), 2):
        tree[nodes[i]].append(nodes[i+1])

    p1 = []
    p2 = []
    find(nodeA, p1)
    find(nodeB, p2)
    res = []
    for i in p1:
        for j in p2:
            if i == j:
                res.append(i)
    cnt = 1
    subtree(res[0])

    print("#{} {} {}".format(t+1, res[0], cnt))