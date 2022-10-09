
from operator import le


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = min(x, 1024 * 64)
        
        while(left <= right):
            mid = left + (right - left) // 2
            if (mid * mid <= x):
                left = mid + 1
            else:
                right = mid - 1
                
        return left-1