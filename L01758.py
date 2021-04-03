class Solution:
  def minOperations(self, s: str) -> int:
    b0 = 0
    b1 = 0
    c0 = False
    c1 = True
    for x in s:
      if int(x) != c0:
        b0 += 1
      if int(x) != c1:
        b1 += 1
      c0 = not c0
      c1 = not c1  
    return min(b0, b1)
  
s = Solution()
print(s.minOperations("0101"))