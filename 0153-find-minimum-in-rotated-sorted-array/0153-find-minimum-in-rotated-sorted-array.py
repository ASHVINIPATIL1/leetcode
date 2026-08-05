class Solution:
    def findMin(self, nums: List[int]) -> int:
        st = 0
        end = len(nums) - 1
        ans = float('inf')

        while st <= end:
            mid = st + (end - st) // 2
            if nums[st] <= nums[mid]:
                ans = min(ans, nums[st])
                st = mid + 1
            else:
                end = mid - 1
                ans = min(ans, nums[mid])
        return ans
            