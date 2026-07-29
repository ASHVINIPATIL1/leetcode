class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        count_curr = 0
        last_smaller = float('-inf')

        for i in range(len(nums)):
            if nums[i] - 1 == last_smaller:
                count_curr += 1
                last_smaller = nums[i]
            elif nums[i] != last_smaller:
                count_curr = 1
                last_smaller =  nums[i]
            longest = max(longest, count_curr)
        return longest