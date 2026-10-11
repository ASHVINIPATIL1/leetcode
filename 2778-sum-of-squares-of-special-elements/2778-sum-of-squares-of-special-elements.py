class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        squaredSum = 0

        for i in range(1, n+1):
            if n % i == 0:
                squaredSum  = squaredSum + (nums[i-1] * nums[i-1])

        return squaredSum

