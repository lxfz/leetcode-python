class Solution:
  def countHomogenous(self, s: str) -> int:
    res = 0
    m = 1000000007
    # for i in range(len(s)):
    #   for j in range(i, len(s)):
    #     if s[i] == s[j]:
    #       # print(i, j)
    #       res += 1
    #     else:
    #       break
    i=0
    j=0
    while(i<len(s) and j<len(s)):
      if(s[i] == s[j]):
        res = (res + (j-i+1) % m ) % m

        print(i, j)
        j+=1
      else:
        i = j
    return res
sl = Solution()
s = "abbcccaa"
print(sl.countHomogenous(s))