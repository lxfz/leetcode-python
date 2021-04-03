class Solution:
  def balancedStringSplit(self, s: str) -> int:
    ans = 0
    count = 0
    for x in s:
      if x == "R":
        count += 1
      else:
        count -= 1
      if(count == 0):
        ans += 1
    return ans

if __name__ == "__main__":
  solution = Solution()
  s = input()
  print(solution.balancedStringSplit(s))