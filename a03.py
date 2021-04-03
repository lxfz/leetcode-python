from typing import List

class Solution:
    def calculateBeauty(self, s):
        a = [0] * 26
        most_freq = 0
        min_feq = 1000
        for c in s:
            idx = ord(c) - ord('a')
            a[idx] += 1
            if a[idx] > most_freq:
                most_freq = a[idx]
            if a[idx] < min_feq:
                min_feq = a[idx]
        if(most_freq > min_feq):
            return most_freq - min_feq
        else:
            return 0
    
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                subs = s[i:j]
                ans += self.calculateBeauty(subs)
                
        return ans
s = Solution()
print(s.beautySum("aabcb"))