class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        dValue = []
        ans = 0

        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j])
                count = len(seen)
                ans = ans + (count * count)
               
        return ans