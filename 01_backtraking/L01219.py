from typing import List

class Solution:
  def __init__(self):
    super().__init__()
    self.ans = 0
    
  def solve(self, x, y, grid, tmpAns):
    gold = grid[x][y]
    grid[x][y] = 0
    tmpAns += gold
    self.ans = max(self.ans, tmpAns)

    # up
    if x-1 >= 0 and grid[x-1][y] > 0:
      self.solve(x-1, y, grid, tmpAns)
    # down
    if x+1 < len(grid) and grid[x+1][y] > 0:
      self.solve(x+1, y, grid, tmpAns)
    # left
    if y-1 >= 0 and grid[x][y-1] > 0:
      self.solve(x, y-1, grid, tmpAns)
    # right
    if y+1 < len(grid[0]) and grid[x][y+1]>0:
      self.solve(x, y+1, grid, tmpAns)
      
    grid[x][y] = gold

  def getMaximumGold(self, grid: List[List[int]]) -> int:
    for x in range(len(grid)):
      for y in range(len(grid[0])):
        self.solve(x, y, grid, 0)
    return self.ans

s = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(s.getMaximumGold(grid))