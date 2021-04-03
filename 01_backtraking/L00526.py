class Solution:
  def __init__(self):
    super().__init__()
    self.ans = 0
    
  def solve(self, k, h, visited):
    visited[h] = True
    if (k == len(visited)-1):
      self.ans += 1
    else:
      for i in range(1, len(visited)):
        if visited[i] == False and (i % (k+1) == 0 or (k+1) % i == 0):
          self.solve(k+1, i, visited)
    visited[h] = False

  def countArrangement(self, n: int) -> int:
    visited = [False] * (n+1)
    for i in range(1, len(visited)):
      self.solve(1, i, visited)
    return self.ans

s = Solution()
print(s.countArrangement(1))