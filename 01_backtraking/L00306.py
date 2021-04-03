class Solution:
  def __init__(self):
    super().__init__()
    self.result = False
  def solve(self, num, l, r, res):
    if self.result:
      return
    if(r - l > 1) and (num[l] == '0'):
      return
    res.append(int(num[l:r]))
    if len(res) > 2:
      if res[-1] == res[-2] + res[-3]:
        if r == len(num):
          self.result =  True
        else:
          for i in range(r+1, len(num)+1):
              self.solve(num, r, i, res)
    else:
      for i in range(r+1, len(num)+1):
          self.solve(num, r, i, res)
    res.pop()
     
  
  def isAdditiveNumber(self, num: str) -> bool:
    for r in range(1, len(num)+1):
        self.solve(num, 0, r, [])
    return self.result

s = Solution()
print(s.isAdditiveNumber("101"))