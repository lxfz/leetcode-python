class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    s, t = t, s
    f = [[False for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)+1):
      f[i][0] = True
    for j in range(1, len(t)+1):
      f[0][j] = False

    for i in range(1, len(s)+1):
      for j in range(1, len(t)+1):
        f[i][j] = f[i-1][j]
        if s[i-1] == t[j-1]:
          f[i][j] = f[i-1][j-1]
    
    return f[len(s)][len(t)]

s = "abc"
t = "ahbgdc"

x = Solution()
print(x.isSubsequence(s, t))