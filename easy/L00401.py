from typing import List

def numOfOne(num):
  count = 0
  while(num != 0):
    num = (num-1)&num
    count += 1
  return count

class Solution:
  def numOfOne(self, num):
    count = 0
    while(num != 0):
      num = (num-1)&num
      count += 1
    return count
  
  def readBinaryWatch(self, num: int) -> List[str]:
    res = []
    n = 1 << 10
    for i in range(n):
      if self.numOfOne(i) == num:
        h = i >> 6
        m = ((1 << 6) -1) & i
        if (h>=0 and h<= 11 and m >=0 and m <=59):
          s = f"{h}:{m:02}"
          res.append(s)
    return res

s = Solution()
num = int(input())
print(s.readBinaryWatch(num))
        