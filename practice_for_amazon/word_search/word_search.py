"""
Given an mxn grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.  The same letter cell may not be used more than once.

Input:
board = [["A"]]

I: mxn grid of character, and a word
O: boolean whether the word is in the grid
C:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.


E:

At each decision, I can do right, or go down.
if there is a character, then I trigger the find?

"""


def exist(board, word):
    """
    :type board: List[ListListt[str]]
    :type word: str
    :rtype: bool
    """
    MAX_ROWS = len(board)
    MAX_COLS = len(board[0])
    path = set()

    def backtracking(row, col, i):
        # if solution:
        # output(solution)
        if i == len(word):
            return True

        # check to make sure the word begins is the same
        # check if we are not out of bound
        if (
            row < 0
            or row >= MAX_ROWS
            or col < 0
            or col >= MAX_COLS
            or board[row][col] != word[i]
            or (row, col) in path
        ):
            return False

        # place a candidate
        path.add((row, col))

        # explore all the choices
        res = (
            backtracking(row - 1, col, i + 1)
            or backtracking(row + 1, col, i + 1)
            or backtracking(row, col + 1, i + 1)
            or backtracking(row, col - 1, i + 1)
        )

        # revert the choice
        path.remove((row, col))
        return res

    # loop through the board to check for where a work start
    for row in range(MAX_ROWS):
        for col in range(MAX_COLS):
            if backtracking(row, col, 0):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
words = "ABCCED"

print(exist(board, words))

"""
time:
O(M x N x backtracking)

backtracking: 4^(L) where L is the length of the word
but we do not go back to where we come from so it is only 3^L

space:
O(L):
"""
