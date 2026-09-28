class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums2)
        res = [-1] * len(nums1)
        stack = []

        for i in range(n-1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                if nums2[i] in nums1:
                    index = nums1.index(nums2[i])
                    res[index] = stack[-1]
            
            stack.append(nums2[i])

        return res

