from typing import List

class Solution:

  def solve(self, k, choseFlag, nums, sett, resultList):
    if choseFlag:
      sett.append(nums[k])
    if k == len(nums) - 1:
      resultList.append(sett.copy())
    if k < len(nums) - 1:
      self.solve(k+1, True, nums, sett, resultList)
      self.solve(k+1, False, nums, sett, resultList)
    if choseFlag:
      sett.pop()
    
  def subsets(self, nums: List[int]) -> List[List[int]]:
    resultList = []
    self.solve(0, True, nums, [], resultList)
    self.solve(0, False, nums, [], resultList)
    return resultList
s = Solution()
nums = [0]
print(s.subsets(nums))
        