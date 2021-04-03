from typing import List

class Solution:
  
  def visit(self, i, s, resList):
    if(i == len(s)):
      resList.append("".join(s))
      return
    
    self.visit(i+1, s, resList)
    if s[i].isupper():
      s[i] = s[i].lower()
      self.visit(i+1, s, resList)
      s[i] = s[i].upper()
    elif s[i].islower():
      s[i] = s[i].upper()
      self.visit(i+1, s, resList)
      s[i] = s[i].lower()
      
  
  def letterCasePermutation(self, S: str) -> List[str]:
    s = list(S)
    resList = []
    self.visit(0, s, resList)
    return resList
  
s = Solution()
print(s.letterCasePermutation("a1b2"))