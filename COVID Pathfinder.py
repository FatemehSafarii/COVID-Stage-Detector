def valid(board, row, column, cc, lc):
    corona = 'CORONA'
    x, y, word = cc
    word = (word + 1) % 6
    output = []

    if x - 1 >= 0 and board[x - 1][y] == corona[word] and (x - 1, y, word) != lc:
        output.append((x - 1, y, word))
    if y - 1 >= 0 and board[x][y - 1] == corona[word] and (x, y - 1, word) != lc:
        output.append((x, y - 1, word))
    if x + 1 < row and board[x + 1][y] == corona[word] and (x + 1, y, word) != lc:
        output.append((x + 1, y, word))
    if y + 1 < column and board[x][y + 1] == corona[word] and (x, y + 1, word) != lc:
        output.append((x, y + 1, word))
    return output


def move(board, row, column):
    branches = [1]
    for i in range(row):
        for j in range(column):
            if board[i][j] == 'C':
                branches.append([(i, j, 0)])

    while len(branches) != 1:
        if len(branches[1]) == 1:
            valid_move = valid(board, row, column, branches[1][-1], (-2, -2, -2))
        else:
            valid_move = valid(board, row, column, branches[1][-1], branches[1][-2])
        length = len(valid_move)
        while length != 0:
            if valid_move[0] in branches[1]:
                return 'Emergency situation. patient should be transferred to ICU.'
            branches[1].append(valid_move[0])
            temp = branches[1][:-1]
            for i in range(1, length):
                if valid_move[i] in temp:
                    return 'Emergency situation. patient should be transferred to ICU.'
                branches.append(temp + [valid_move[i]])
            valid_move = valid(board, row, column, branches[1][-1], branches[1][-2])
            length = len(valid_move)

        branches[0] = max(branches[0], len(branches[1]))
        del branches[1]
    number = branches[0] // 6
    if number == 0:
        return 'Patient is healthy and ready to dismiss.'
    return number


_row = input().split(' ')
_column = int(_row[1])
_row = int(_row[0])
_board = []
for _i in range(_row):
    _board.append(list(input()))
print(move(_board, _row, _column))
