class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if (i == 0 or nums[i - 1] < nums[i]) and (i == (len(nums) - 1) or nums[i] > nums[i + 1]):
                return i
            if nums[i] > nums[i - 1] and nums[i] > nums[i+1]:
                return i
        # peak = 0
        # st = 1
        # end = len(nums) - 2
        # while st <= end:
        #     mid = (st - end) // 2

        #     if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
        #         return mid
            