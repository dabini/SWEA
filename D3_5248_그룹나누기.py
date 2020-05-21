def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x] += 1

def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    peers = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    for i in range(M):
        union(peers[2*i], peers[2*i+1])
    group = set()
    for j in range(1, N+1):
        group.add(find_set(j))
    print("#{} {}".format(t+1, len(group)))