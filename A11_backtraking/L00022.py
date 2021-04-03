from typing import List

class Solution:
  
  def solve(self, n, n_left, res, resList):
    if(n == 0):
      resList.append("".join(res))
      return
    # n > 0
    if(n_left == 0):
      res.append("(")
      self.solve(n, n_left+1, res, resList)
      res.pop()
    elif(n_left < n):
      res.append("(")
      self.solve(n, n_left+1, res, resList)
      res.pop()
      
      res.append(")")
      self.solve(n-1, n_left-1, res, resList)
      res.pop()
    else:
      res.append(")")
      self.solve(n-1, n_left-1, res, resList)
      res.pop()
  
  def solve_v2(self, append_char, n, n_left, n_right, res, resList):
    res.append(append_char)
    if(n_left + n_right == 2 * n):
      resList.append("".join(res))
    else:
      if n_left < n:
        self.solve_v2("(", n, n_left+1, n_right, res, resList)
      if n_right < n_left:
        self.solve_v2(")", n, n_left, n_right+1, res, resList)
    res.pop()
    
  def solve_v3(self, n, n_left, n_right, res, resList):
    if(n_left + n_right == 2*n):
      resList.append(res)
    else:
      if n_left < n:
        self.solve_v3(n, n_left+1, n_right, res+"(", resList)
      if n_right < n_left:
        self.solve_v3(n, n_left, n_right+1, res+")", resList)
      
            
      
  def generateParenthesis(self, n: int) -> List[str]:
    resList = []
    # self.solve(n, 0, [], resList)
    self.solve_v3(n, 1, 0, "(", resList)
    return resList

s = Solution()
print(s.generateParenthesis(3))