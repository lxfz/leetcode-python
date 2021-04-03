class Solution:
  def __init__(self):
    super().__init__()
    self.result = False
  
  def solve(self, addFlag, k, sm, target):
    if self.result or k>16:
      return
    if addFlag:
      sm += 3**k
    if(sm == target):
      self.result = True
    elif(sm < target):
      self.solve(False, k+1, sm, target)
      self.solve(True, k+1, sm, target)  
  
  def checkPowersOfThree(self, n: int) -> bool:
    self.solve(False, 0, 0, n)
    self.solve(True, 0, 0, n)
    return self.result

s = Solution()
print(s.checkPowersOfThree(91))