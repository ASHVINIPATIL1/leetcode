class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1
            
            for i in range(low, high + 1):
                nums[i] = temp[i - low]
        
        def countPairs(low, mid, high):
            right = mid + 1
            cnt = 0

            for left in range(low, mid + 1):
                while right <= high and nums[left] > 2 * nums[right]:
                    right += 1
                cnt += right - (mid+1)

            return cnt

        def mergeSort(low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            cnt = mergeSort(low, mid)
            cnt += mergeSort(mid + 1, high)
            cnt += countPairs(low, mid, high)
            merge(low, mid, high)

            return cnt

        return mergeSort(0, len(nums) - 1)