

def all_marked(board):
    for row in board:
        if len(list(filter(lambda x: x > 0, row))) == 0:
            return True
    return False


def has_won(board):
    return all_marked(board) or all_marked(list(zip(*board)))


def mark(inp, board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == inp:
                board[i][j] *= -1
                return board
    return board


def play(inputs, boards):
    for (ii, inp) in enumerate(inputs):
        for (bi, board) in enumerate(boards):
            if has_won(mark(inp, board)):
                return (board, bi,  inp, ii)


def answer():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n\n")
        inputs = list(map(int, lines[0].split(",")))
        boards = [[[int(y) for y in x.split()]
                   for x in board.split("\n")] for board in lines[1:]]
        (won_board, _, winning, _) = play(inputs, boards)

        print(sum(filter(lambda x: x > 0, sum(won_board, [])))*winning)


def answer2():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n\n")
        inputs = list(map(int, lines[0].split(",")))
        boards = [[[int(y) for y in x.split()]
                   for x in board.split("\n")] for board in lines[1:]]
        while len(boards) > 0:
            (won_board, bi, winning, wi) = play(inputs, boards)
            boards.pop(bi)
            inputs = inputs[wi:]

        print(sum(filter(lambda x: x > 0, sum(won_board, [])))*winning)


answer()
answer2()
