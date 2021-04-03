class Solution:
  def divisorGame(self, n: int) -> bool:
    f = [False] * (n+2)
    f[2] = True
    for i in range(3, n+1):
      for j in range(1, i):
        if i % j == 0 and f[i-j]==False:
          f[i] = True
          break
    return f[n]

s = Solution()
print(s.divisorGame(1))
          
        