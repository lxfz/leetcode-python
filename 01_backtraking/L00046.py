from typing import List

class Solution:
  
  def solve(self, nums, i, res, resList):
    res.append(nums[i])
    if(len(res) == len(nums)):
      resList.append(res.copy())
    else:
      for k in range(len(nums)):
        if nums[k] not in res:
          self.solve(nums, k, res, resList)
    res.pop()
  
  def permute(self, nums: List[int]) -> List[List[int]]:
    resList = []
    for k in range(len(nums)):
      self.solve(nums, k, [], resList)
    return resList

s = Solution()
nums = [1,2,3]
print(s.permute(nums))