class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                c += int(a[i])
                i -= 1
            if j >= 0:
                c += int(b[j])
                j -= 1
            ans.append(str(c % 2))
            c //= 2

        if c != 0:
            ans.append(str(c))
        return "".join(ans)[::-1]


s = Solution()
a = "1010"
b = "1011"

print(s.addBinary(a, b))
