from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for x in range(len(nums)):
            if (x != 0 and nums[x] == nums[x-1]): continue
            for y in range(x+1, len(nums)):
                if (y != x+1 and nums[y] == nums[y-1]): continue
                i = y+1
                j = len(nums) - 1
                while (i < j):
                    if i != y+1 and nums[i] == nums[i-1]: 
                        i += 1
                        continue
                    if j != len(nums) - 1 and nums[j] == nums[j+1]: 
                        j -= 1
                        continue
                    s = nums[x] + nums[y] + nums[i] + nums[j]
                    if s > target:
                        j -= 1
                    elif s < target:
                        i += 1
                    else:
                        ans.append([nums[x], nums[y], nums[i], nums[j]])
                        i += 1
                        j -= 1
        return ans
