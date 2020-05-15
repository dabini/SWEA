field = [[0] * 300 for _ in range(300)]
for i in range(1, 300):
    field[i][1] = field[i - 1][1] + i

for i in range(1, 300):
    for j in range(2, 300):
        field[i][j] = field[i][j - 1] + i + (j - 2)

for tc in range(1, int(input())+1):
    p, q = map(int, input().split())
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(1, 300):
        if x1 and y1 and x2 and y2:
            break
        for j in range(1, 300):
            if field[i][j] == p:
                x1, y1 = i, j
            if field[i][j] == q:
                x2, y2 = i, j
    res = field[x1 + x2][y1 + y2]
    print(f"#{tc} {res}")