from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        mindist = float("inf")
        for i, point in enumerate(points):
            if(point[0] == x or point[1] == y):
                if(abs(point[0] - x) + abs(point[1] - y) < mindist):
                    mindist = abs(point[0] - x) + abs(point[1] - y)
                    ans = i
        return ans

s = Solution()
x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(s.nearestValidPoint(x, y, points))