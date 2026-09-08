class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 

        n = len(nums)
        zeros = 0
        maxLen = 0 

        l = 0
        r = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                cLen = r - l + 1
                maxLen = max(cLen, maxLen)
            r += 1 
        return maxLen


        