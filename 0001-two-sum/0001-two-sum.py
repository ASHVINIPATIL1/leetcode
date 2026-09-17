class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            remaining = target - nums[i]
            if remaining in nums and nums.index(remaining) != i:
                return [i, nums.index(remaining)]