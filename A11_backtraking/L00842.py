from typing import List

class Solution:
  def __init__(self):
    super().__init__()
    self.ans = []
    
  def solve(self, s, begin, end, res):
    if self.ans != []:
      return
    
    tstr =  s[begin:end]
    if len(tstr) > 1 and tstr[0] == '0' or int(tstr) >= (1<<31):
      return
    
    res.append(int(tstr))
    if end == len(s):
      if len(res)>2 and res[-1] == res[-2] + res[-3]:
        self.ans = res.copy()
    elif len(res)>2 and res[-1] == res[-2] + res[-3] or len(res) <= 2:
      for i in range(end+1, len(s)+1):
        self.solve(s, end, i, res)
    res.pop()
    
  def splitIntoFibonacci(self, S: str) -> List[int]:
    for end in range(1, len(S)+1):
      self.solve(S, 0, end, [])
    return self.ans
  
s = Solution()
S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
# "539834657 21 539834678 539834699 1079669377 1619504076 2699173453 4318677529 7017850982 11336528511"
# [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
print(s.splitIntoFibonacci(S))