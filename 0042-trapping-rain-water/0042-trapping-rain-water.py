class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        lMax = rMax = total = 0
        l = 0
        r = n-1

        while l < r:
            if height[l] <= height[r]:
                if height[l] < lMax:
                    total += lMax - height[l]
                else:
                    lMax = height[l]
                l = l + 1
            else:
                if height[r] < rMax:
                    total += rMax - height[r]
                else:
                    rMax = height[r]
                r = r - 1
            
        return total
