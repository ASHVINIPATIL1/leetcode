class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = 0
        result = float('inf')
        summ = 0

        while j < n:
            summ = summ + nums[j]
            while summ >= target:
                lenn = j - i + 1
                result = min(result, lenn)
                summ = summ - nums[i]
                i += 1
            j += 1
        return 0 if result == float("inf") else result
            