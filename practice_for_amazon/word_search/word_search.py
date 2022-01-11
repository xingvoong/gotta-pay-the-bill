'''
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

'''

def exist(board, word):
  """
  :type board: List[ListListt[str]]
  :type word: str
  :rtype: bool
  """
  MAX_ROWS = len(board)
  MAX_COLS = len(board[0])

  def backtracking(row, col, remain_word):
    # if solution:
    # output(solution)
    if len(remain_word) == 0:
      return True

    # visit all the next candidates
    # which is the 4 neighbors
    toReturn = False
    for x in range(row - 1, row + 2):
      for y in range(col - 1, col + 2):
        if -1 < x < MAX_ROWS and -1 < y < MAX_COLS and x != row and y != col and board[x][y] == remain_word[0]:
          print("x", x)
          print("y", y)
          print(remain_word[1:])
          # place the next candidate
          board[x][y] = "#"

          # backtracking
          # print(backtracking(x, y, remain_word[1:]))

          toReturn = backtracking(x, y, remain_word[1:])
          if toReturn:
            break

          # revert the choice
          board[x][y] = remain_word[0]

          return toReturn

  # loop through the board to check for where a work start
  for row in range(MAX_ROWS):
    for col in range(MAX_COLS):
      if backtracking(row, col, word):
        return True

  return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
words = "ABCCED"

print(exist(board, words))
