class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st = 0
        end = n -1

        while st <= end:
            mid = st + (end - st)//2
            if mid == 0 | mid == (n - 1):
                return nums[mid]
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid - 1] == nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid - 1] == nums[mid]:
                    st = mid + 1
                else: 
                    end = mid - 1
        # return nums[mid]