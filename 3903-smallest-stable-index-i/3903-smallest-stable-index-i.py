class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        stability = []

        for i in range(n):
            stab = max(nums[:i+1]) - min(nums[i:])
            stability.append(stab)

        for i in stability:
            if i <= k:
                return stability.index(i)

        return -1