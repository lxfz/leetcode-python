class Solution:
  def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
    maxLen = 0
    ans = 0
    for rec in rectangles:
      side = min(rec)
      if(side == maxLen):
        ans += 1
      elif(side > maxLen):
        maxLen = side
        ans = 1
    return ans          