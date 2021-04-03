from typing import List


class Solution:
  
  def solve(self, h, res, k, n, resList):
    res.append(h)
    if(len(res) == k):
      if(sum(res) == n):
        resList.append(res.copy())
    elif(sum(res) < n):
      for i in range(h+1, 10):
        self.solve(i, res, k, n, resList)
    res.pop()
    
  
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    resList = []
    for i in range(1, 10):
      self.solve(i, [], k, n, resList)
    return resList

s = Solution()
print(s.combinationSum3(9, 46))