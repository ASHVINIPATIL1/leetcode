class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            sum_digits = 0
            while n > 0:
                digit = n % 10
                sum_digits += digit
                n //= 10
            if i == sum_digits:
                return i
        return -1