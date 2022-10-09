
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # TODO: KMP
        return haystack.find(needle)




s = Solution()
print(s.strStr(haystack = "leetcode", needle = "e"))