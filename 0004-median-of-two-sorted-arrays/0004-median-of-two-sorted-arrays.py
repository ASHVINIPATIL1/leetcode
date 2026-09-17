class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merged = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < m:
            merged.extend(nums1[i:])

        if j < n:
            merged.extend(nums2[j:])
        
        l = len(merged)

        if l % 2 != 0:
            return merged[l//2]
        else:
            return (merged[(l//2) - 1] + merged[l//2]) / 2

