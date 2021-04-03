class Solution:
  def countVowelStrings(self, n: int) -> int:
    f = [ [ 0 for _ in range(5)] for __ in  range(n+1) ]
    for i in range(5):
      f[1][i] = 1
    for i in range(2, n+1):
      for j in range(5):
        for k in range(j+1):
          f[i][j] += f[i-1][k]
    ans = 0
    for j in range(5):
      ans += f[n][j]
    return ans

s = Solution()
print(s.countVowelStrings(33))