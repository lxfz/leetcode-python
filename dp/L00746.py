from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    f = [0] * (len(cost) + 1)
    for i in range(2, len(f)):
      f[i] = min(f[i-1]+cost[i-1], f[i-2]+cost[i-2])
    return f[-1]

cost = [10, 15]
s = Solution()
print(s.minCostClimbingStairs(cost))