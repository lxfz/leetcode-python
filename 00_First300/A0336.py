from typing import List
import string

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        Map = {word: i for i, word in enumerate(words)}
        ans = []
        
        for i, word in enumerate(words):
            reverse_word = word[::-1]
            if reverse_word in Map and i != Map.get(reverse_word):
                ans.append([i, Map.get(reverse_word)])
            if reverse_word[1:] in Map and i != Map.get(reverse_word[1:]):
                ans.append([i, Map.get(reverse_word[1:])])
            
            for prefix in string.ascii_lowercase:
                new_word = prefix + reverse_word
                if new_word in Map and i != Map.get(new_word):
                    ans.append([i, Map.get(new_word)])
    
        return ans
    
    
s = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(words))