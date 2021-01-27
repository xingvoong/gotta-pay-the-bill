'''
1. medium, backtracking

2. problem statement

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
exp 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCCED"
Output: true
exp 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "SEE"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
word = "ABCB"
Output: false

3. solution in plain English/ pseudocode
+ intuition:
    we loop through all the cell of the grid,
    at each cell, we call backtracking function to see
    whether we can obtain a solution from the cell
+ backtrack():
    1: base case for recursion:
        the word to be match is empty means
        we have found all the prefix for the word
    2: check whether the current state is valid:
        not out of bound
        the current cell contains the desired character
        + if valid:
            move forward
    3: start exploring with backtracking
        mark visited cell
        explore the 4 possible directions, up, down, left, right
        + if we find the word:
            break out of the loop
    4: revert the word back to it original state
        return the result
'''


class word_search(object):
    def word_exist(self, board, word):
        # CONSTANT
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, suffix):

        if len(suffix) == 0:
            return True
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        toReturn = False
        self.board[row][col] = '#'
        for row_offset, col_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            toReturn = self.backtrack(row + row_offset,
                                      col + col_offset, suffix[1:])

            if toReturn:
                break
        self.board[row][col] = suffix[0]
        return toReturn


test = word_search()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
words = ["ABCCED", "SEE", "ABCB"]
expected = [True, True, False]
for i in range(len(words)):
    assert test.word_exist(board, words[i]) == expected[i]

'''
5. runtime analysis:
let N the number of cells in the board
L is the length of the searched word.
runtime: O(N.3^L)
+ for backtracking:
    the first cell has 4 moves
    but the next cell has only 3 moves
    because we don't go back to the previous cell
    there are at most 3^L of possibles for a word of length L
+ we call backtracking at most N time:
    once for each cell

space: O(L)
recursive stack for backtracking function
'''
