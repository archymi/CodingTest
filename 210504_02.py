# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, number in enumerate(nums):
            if (target - number) in nums[index+1:]:
                return [index, nums[index+1:].index(target - number) + index + 1]
        return [0, 0]


tmp = Solution()
#print(tmp.twoSum([2, 7, 11, 15], 9))
#print(tmp.twoSum([3, 2, 4], 6))
print(tmp.twoSum([3, 3], 6))