from typing import List

class Solution:
  def __init__(self):
    super().__init__()
    self.ans = 0
  def solve(self, groupid, visited, remain, num_happy, batchSize, groups):
    visited.append(groupid)
    if(remain==0):
      num_happy += 1
    if(len(groups) - self.ans < len(visited) - num_happy):
      visited.pop()
      return
    if(len(visited) == len(groups)):
      self.ans = max(self.ans, num_happy)
      # print(self.ans, "\t" , visited)
    else:
      if(groups[groupid] <= remain):
        remain -= groups[groupid]
      else:
        remain = (groups[groupid] - remain) % batchSize
        if(remain > 0):
          remain = batchSize - remain
      # print(remain)
      for i in range(len(groups)):
        if i not in visited:
          self.solve(i, visited, remain, num_happy, batchSize, groups)
    visited.pop()
  
  def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
    ng = [x for x in groups if x % batchSize != 0]
    for i in range(len(ng)):
      self.solve(i, [], 0, 0,batchSize, ng)
    return self.ans + len(groups) - len(ng)

sl = Solution()
batchSize = 1
groups = [909925048,861425549,820096754,67760437,273878288,126614243,531969375,817077202,482637353,507069465,699642631,407608742,846885254,225437260,100780964,523832097,30437867,959191866,897395949]
print(len(groups))
print(sl.maxHappyGroups(batchSize, groups))