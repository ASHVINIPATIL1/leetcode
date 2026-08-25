class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # mult = []
        # n = max(nums) + k
        # for i in range(k, n + 1, k):
        #     mult.append(i)

        # for m in mult:
        #     if m not in nums:
        #         return m
        
        i = 1
        while True:
            if i * k not in nums:
                return i * k
            else:
                i += 1