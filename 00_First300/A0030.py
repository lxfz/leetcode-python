from typing import List
import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        k = len(words)
        size = len(words[0])
        word_count = collections.Counter(words)

        for i in range(n - k*size+1):
            count = word_count.copy()
            word_used = 0
            for j in range(i, i + k * size, size):
                sub = s[j: j+size]
                if count[sub] > 0:
                    count[sub] -= 1
                    word_used += 1
                else:
                    break
            if word_used == k:
                ans.append(i)
        
        return ans
                