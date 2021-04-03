from typing import List

class Solution:
  def reverse(self, x):
    res = 0
    while(x>0):
      res = res * 10 + x % 10
      x //= 10
    return res
  
  def countNicePairs(self, nums: List[int]) -> int:
    revNums = [0] * len(nums)
    for i in range(len(nums)):
      revNums[i] = self.reverse(nums[i])
      revNums[i] = nums[i] - revNums[i]
    revNums.sort()
    i = 0
    j = 1
    ans = 0
    m = 10**9 + 7
    while(j<len(revNums)):
      if(revNums[i] == revNums[j]):
        ans = (ans + j - i) % m
      else:
        i = j
      j+=1
    return ans

sl = Solution()
nums = [42,11,1,97]
print(sl.countNicePairs(nums))
