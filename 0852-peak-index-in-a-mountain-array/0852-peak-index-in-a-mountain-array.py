class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # for i in range(len(arr)):
        #     if arr[i] > arr[peak]:
        #         peak = i
        # return peak

        st = 1
        end = len(arr)-2

        while st <= end:
            mid = st + (end-st)//2

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            if arr[mid - 1] < arr[mid]:
                st = mid + 1
            else:
                end = mid - 1

