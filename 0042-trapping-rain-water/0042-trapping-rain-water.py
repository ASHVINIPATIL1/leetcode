class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        prefix = [0] * n
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])

        water = 0
        suffix = height[n-1]

        for i in range(n-2, -1, -1):
            suffix = max(suffix, height[i])

            waterLevel = min(prefix[i], suffix)

            if height[i] < waterLevel:
                water += waterLevel - height[i]

        return water 
        



