class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # calculate sum of all numbers from 1 to n
        summ = n * (n + 1) // 2

        arrsum = 0
        # calculat sum of all numbers in arr
        for i in range(n):
            arrsum += nums[i]
        # eg: summ = 16 arr = [1, 2, 3, 5] missing = 4
        # 16 - 11 = 4
        return summ - arrsum
        