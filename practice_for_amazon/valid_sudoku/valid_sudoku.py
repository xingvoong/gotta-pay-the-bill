"""
Determine if a 9x9 Sudoku board is valid.  Only the filled cells need to be validated according to the following rules.

1:  Each row must contain the digits 1-9 without repetition
2:  Each row must contain the digits 1-9 with out repetition
3: each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition

Note:

- A sudoku board (partially filled) could be valid but is not necessariy solvable
- Only the filled cells need to be validated according to the mentioned rules

Compare:  the other question a full filled board,
and the task is to check whether that is a solution

This one is not partially filled
and the task is to check whether it is valid (not neccessary solvable)

"""


def isValidSudoku(board):
    MAX_ROWS = len(board)
    MAX_COLS = len(board[0])

    def isValid(array):
        count = {}
        for i in array:
            if i.isdigit():
                toInt = int(i)
                if toInt in range(1, 10):
                    if toInt in count:
                        return False
                    else:
                        count[toInt] = 1
                else:
                    return False

        if len(count) == 0:
            return False

        return True

    # validate rows
    for i in range(MAX_ROWS):
        a_row = []
        for j in range(MAX_COLS):
            a_row.append(board[i][j])
        if not isValid(a_row):
            return False

    # validate cols
    for j in range(MAX_COLS):
        a_col = []
        for i in range(MAX_ROWS):
            a_col.append(board[i][j])
        if not isValid(a_col):
            return False

    # # are 3x3 subboxs valid:
    # # start of 9 subbox:
    # # (0, 0) (0, 3) (0, 6)
    # # (3, 0) (3, 3) (3, 6)
    # # (6, 0) (6, 3) (6, 6)

    subbox_start = [
        (0, 0),
        (0, 3),
        (0, 6),
        (3, 0),
        (3, 3),
        (3, 6),
        (6, 0),
        (6, 3),
        (6, 6),
    ]
    for start in subbox_start:
        subbox = []
        for i in range(start[0], start[0] + 3):
            for j in range(start[1], start[1] + 3):
                subbox.append(board[i][j])
        if not isValid(subbox):
            return False

    return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

board3 = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "9", ".", ".", ".", ".", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "9", "9", "3", "5", "7", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "4", "."],
    [".", ".", ".", "8", ".", ".", ".", ".", "."],
    [".", "1", ".", ".", ".", ".", "4", ".", "9"],
    [".", ".", ".", "5", ".", "4", ".", ".", "."],
]

board4 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board5 = [[".", ".", ".", ".", ".", ".", ".", ".", "."]]
print(isValidSudoku(board4))


"""
let N be the dimension of the board

time: O(N^2)

isValid: O(N)
check for row:


space:
isValid: O(N^2) space

if the board is fix size, then N = 9
=> this arguably I can say O(1)
"""
