from typing import List
import string

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        Map = {num : i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in Map and i != Map.get(target - num):
                return [i, Map.get(target - num)]
        
        return -1


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        
        while(i < j):
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        
        return -1
                
        


s = Solution()
nums = [3,2,4]
target = 6

print(s.twoSum(nums, target))