class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n

        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        # front
        dele_f = 0
        f = max(max_index , min_index)
        dele_f = f + 1
        
        # back
        dele_b = 0
        b = min(max_index, min_index)
        dele_b = n - b


        # both
        d = 0
        bo_m = max(max_index, min_index)
        bo_min = min(max_index, min_index)
        dele_bo = n - bo_m
        dele_bo_f = bo_min + 1
        d = dele_bo + dele_bo_f

        return min(dele_f, dele_b, d)