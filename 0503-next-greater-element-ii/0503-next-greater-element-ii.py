class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        stack = []

        for i in range(2*n - 1, -1, -1 ):
            while stack and stack[-1] <= nums[i % n]:    
                stack.pop()    

            if i < n:
                res[i] = -1 if not stack else stack[-1] 
            stack.append(nums[i % n])
        return res