from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstOcc():
            first = 0
            last = len(nums) - 1
            ans = -1

            while first <= last:
                mid = (first + last) // 2
                if nums[mid] == target:
                    ans = mid
                    last = mid - 1  # search left
                elif nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
            return ans
        
        def lastOcc():
            first = 0
            last = len(nums) - 1
            ans = -1

            while first <= last:
                mid = (first + last) // 2

                if nums[mid] == target:
                    ans = mid
                    first = mid + 1  # search right
                elif nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
            return ans

        return [firstOcc(), lastOcc()]
 