from typing import List

class Solution:
    
    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
    
    def solve(self, expression, i, j, dp):
        
        if len(dp[i][j]) != 0:
            return dp[i][j]
        
        if j - i <2:
            dp[i][j] =  [int(expression[i:j+1])]  
            x = dp[i][j]         
            return dp[i][j]
        
        for k in range(i, j):
            op = expression[k]
            # 以运算符作分割            
            if op in ['+', '-', '*']:
                left = self.solve(expression, i, k-1, dp)
                right = self.solve(expression, k+1, j, dp)
                for ll in left:
                    for rr in right:
                        dp[i][j].append(self.calculate(ll, rr, op))
        return dp[i][j]    
        
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        dp = [[[] for j in range(n)] for i in range(n)]
        self.solve(expression, 0, n-1, dp)
        return dp[0][n-1]

# s = Solution()
# expression = "2*3-4*5"
# print(s.diffWaysToCompute(expression))