class Solution:
  def __init__(self):
    super().__init__()
    self.happy_characters = ["a", "b", "c"]
    self.order = 0
    self.ans = ""
  
  def backtrack(self, i, res):
    res.append(self.happy_characters[i])
    if(len(res) == self.n):
      self.order += 1
      if(self.order == self.k):
        self.ans = "".join(res)
    elif len(res) < self.n:
      for j in range(len(self.happy_characters)):
        if i != j:
          self.backtrack(j, res)
    res.pop()
    
  def getHappyString(self, n: int, k: int) -> str:
    self.n = n
    self.k = k
    for i in range(len(self.happy_characters)):
      self.backtrack(i, [])
    return self.ans

s = Solution()
print(s.getHappyString(10, 100))