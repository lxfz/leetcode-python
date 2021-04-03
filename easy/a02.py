from typing import List
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        f = [0] * 15
        f = [f] * (n+2)
        f[0][0] = True
        f[0][1] = True
        for i in range(1, 15):
            for j in range(1, n+1):
                f[i][j] = f[i-1][j]
                if (j - 3**i >0):
                    f[i][j] = f[i][j] or f[i-1][j-3**i]
        return f[14][n]

s = Solution()
print(s.checkPowersOfThree(12))
