class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        left = min(max_index, min_index)
        right = max(max_index, min_index)

        # front
        dele_f = right + 1
        
        # back
        dele_b = n - left


        # both
        d = (n - right) + (left + 1)

        return min(dele_f, dele_b, d)