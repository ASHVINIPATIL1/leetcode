class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        st = 0
        end = len(nums) - 1

        while st <= end:
            mid = st + (end-st)//2
            if nums[mid] == target:
                return True
            if nums[st] == nums[mid] == nums[end]:
                st += 1
                end -= 1
                continue

            if nums[st] <= nums[mid]:  # left part is sorted
                if nums[st] <= target & target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:  # right part is sorted
                if nums[mid] <= target & target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1
        
        return False