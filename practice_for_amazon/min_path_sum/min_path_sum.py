"""
Given a mxn grid filled with non-negative numbers, find a path from top left to bottom right, whcih minumizes the sum all all numbers along its path.
Note:  you can only move either down or right at any point in time.
# at any point, I only consider down and right until I reach the final
Constraints:
- m ==  grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100
"""


def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    MAX_ROWS = len(grid)
    MAX_COLS = len(grid[0])
    # create a db table
    db = [[0 for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]

    # fill the db table: min(top, left, current_cell)
    for i in range(0, MAX_ROWS):
        for j in range(0, MAX_COLS):
            if i - 1 >= 0:
                top = db[i - 1][j]
            else:
                top = 2 ** 31

            if j - 1 >= 0:
                left = db[i][j - 1]
            else:
                left = 2 ** 31

            if i - 1 == -1 and j - 1 == -1:
                top = 0
                left = 0

            db[i][j] = grid[i][j] + min(left, top)

    return db[MAX_ROWS - 1][MAX_COLS - 1]


print(minPathSum([[1, 2]]))