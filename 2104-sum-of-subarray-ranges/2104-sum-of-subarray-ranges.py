class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        summ = 0

        for i in range(len(nums)):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                summ += (maxi - mini)
        return summ