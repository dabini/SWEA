def block(m, n, board, visited):
    for i in range(m - 1):
        for j in range(1, n):
            if board[i][j] != ' ' and board[i][j] == board[i][j - 1] and board[i][j - 1:j + 1] == board[i + 1][
                                                                                                  j - 1:j + 1]:
                visited[i][j] = True
                visited[i][j - 1] = True
                visited[i + 1][j] = True
                visited[i + 1][j - 1] = True


def delete(m, n, board, visited):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == True:
                cnt += 1
                board[i] = board[i][:j] + ' ' + board[i][j + 1:]

    check_board = []
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += board[j][i]
        check_board.append(tmp)

    for i in range(n):
        for j in range(1, m):
            if check_board[i][j] == ' ':
                check_board[i] = ' ' + check_board[i][:j] + check_board[i][j + 1:]

    tmp_board = []
    for i in range(m):
        tmp = ''
        for j in range(n):
            tmp += check_board[j][i]
        tmp_board.append(tmp)

    board = tmp_board

    return board, cnt


def solution(m, n, board):
    answer = 0
    res = 1
    while res:
        visited = [[0] * n for _ in range(m)]
        block(m, n, board, visited)
        board, res = delete(m, n, board, visited)
        answer += res
    return answer

ex1 = 4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
ex3 = (6, 6, ['AAAAAA', 'BBAATB', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA'])
print(solution(*ex3))