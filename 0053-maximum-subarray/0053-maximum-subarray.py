class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l = len(nums)
        maxSum = -10000
        currentSum = 0

        for i in range(l):
            currentSum += nums[i]
            maxSum = max(currentSum, maxSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum
                