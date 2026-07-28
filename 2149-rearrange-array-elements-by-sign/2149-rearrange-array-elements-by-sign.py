class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        num = [0] * len(nums)
        p = 0
        n = 1

        for x in nums:
            if x > 0:
                num[p] = x
                p += 2
            else:
                num[n] = x
                n += 2 

        return num