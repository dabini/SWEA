T = int(input())

for t in range(10):
    puzzle =[[0]*9 for _ in range(9)]

    for i in range(9):
        puzzle[i] = list(map(int, input().split()))

    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = 1
    for y in range(9):
        empty_y = []
        empty_x = []
        for x in range(9):
            empty_y += [puzzle[y][x]]
            empty_x += [puzzle[x][y]]

        if check != sorted(empty_y):
            res = 0
        if check != sorted(empty_x):
            res = 0

    for y in range(0, 6, 3):
        for x in range(0, 6, 3):
            empty = []
            empty += [puzzle[x][y] , puzzle[x][y+1], puzzle[x][y+2], puzzle[x+1][y] , puzzle[x+1][y+1], puzzle[x+1][y+2],puzzle[x+2][y] , puzzle[x+2][y+1], puzzle[x+2][y+2] ]

            if check != sorted(empty):
                res = 0

    print("#{} {}".format(t+1, res))