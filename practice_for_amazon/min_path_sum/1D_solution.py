'''

'''
def minPathSum(grid):
  """
  :type grid: List[List[int]]
  :rtype: int

  """
  MAX_ROWS = len(grid)
  MAX_COLS = len(grid[0])

  dp = [2**31 for _ in range(MAX_COLS + 1)]
  dp[0] = 0
  for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
      print(dp)
      print("grid[i][j]", grid[i][j])
      print("dp[j]", dp[j])
      print("dp[j+1]", dp[j+1])
      print()
      dp[j] = grid[i][j] +  min(dp[j], dp[j-1])


  print(dp)

  return dp[-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
grid2 = [[1,2,3],[4,5,6]]
example = [[1,2],[1,1]]
example2 = [[1, 2]]
print(minPathSum(example))

'''
min(current, and previous one)
so I need to set current equal to something big

time: O(MxN)
space: O(N)

'''