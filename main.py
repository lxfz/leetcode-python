from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
      ans=-1
      topping_first = [0] + toppingCosts
      topping_scond = [0] + toppingCosts
      for b in baseCosts:
        for t1 in topping_first:
          for t2 in topping_scond:
            tmpAns = b + t1 + t2
            if(abs(target - ans) > abs(target - tmpAns)):
              ans = tmpAns
            elif(abs(target - ans) == abs(target - tmpAns)):
              ans = tmpAns if tmpAns < ans else ans
      return ans

if __name__ == "__main__":
  s = Solution()
  baseCosts = [2,3]
  toppingCosts = [4,5,100]
  target = 18
  print(s.closestCost(baseCosts, toppingCosts, target))