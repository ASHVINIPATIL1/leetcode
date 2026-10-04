class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        merged = []
        i = 0
        j = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < n:
            merged.extend(nums1[i:])

        if j < m:
            merged.extend(nums2[j:])

        l = len(merged)

        if len(merged) % 2 != 0:
            return merged[l // 2]
        else: 
            return (merged[(l // 2) - 1] + merged[(l // 2)]) / 2
              