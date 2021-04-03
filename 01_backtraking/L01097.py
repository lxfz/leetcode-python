class Solution:
  def __init__(self):
    super().__init__()
    self.ans = 0
  
  def search(self, m):
    for k, v in m.items():
      # print(k, v)
      if v != 0:
        self.ans += 1
        m[k] -= 1
        self.search(m)
        m[k] += 1
  
  def numTilePossibilities(self, tiles: str) -> int:
    m = {}
    for c in tiles:
      if c in m:
        m[c] += 1
      else:
        m[c] = 1
    # print(m)
    self.search(m)
    
    return self.ans

s = Solution()
print(s.numTilePossibilities("AAABBC"))
       