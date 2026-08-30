class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n

        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        # front
        dele_f = 0
        if max_index > min_index:
            dele_f = max_index + 1

        elif min_index > max_index:
            dele_f = min_index + 1
        
        # back
        dele_b = 0
        if max_index < min_index:
            dele_b = n - max_index

        elif min_index < max_index:
            dele_b = n - min_index

        # both
        d = 0
        if max_index > min_index:
            dele_bo = n - max_index
            dele_bo_f = min_index + 1
            d = dele_bo + dele_bo_f

        elif max_index < min_index:
            dele_bo = n - min_index
            dele_bo_f = max_index + 1
            d = dele_bo + dele_bo_f

        return min(dele_f, dele_b, d)