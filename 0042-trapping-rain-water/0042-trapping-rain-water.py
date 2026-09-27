class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        prefix = [0] * n
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])

        suffix = [0] * n
        suffix[n - 1] = height[n - 1]

        for i in range(n-2, -1, -1):
            suff= max(suffix[i+1], height[i])
            if suff < prefix[i]:
                suffix[i] = suff
            else:
                suffix[i] = prefix[i]

        water = 0

        for i in range(n):
            leftMax = prefix[i]
            rightMax = suffix[i]

            if height[i] < leftMax and height[i] < rightMax:
                water += suffix[i] - height[i]

        return water 
        



