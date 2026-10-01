class Solution:
    def findNSE(self, heights):
        n = len(heights)
        nse = [n] * n
        st = []

        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        return nse

    def findPSE(self, heights):
        n = len(heights)
        pse = [-1] * n
        st = []

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            st.append(i)
        return pse

    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        maxArea = 0
        nse = self.findNSE(heights)
        pse = self.findPSE(heights)

        for i in range(n):
            maxArea = max(maxArea, heights[i] * (nse[i] - pse[i] - 1))

        return maxArea
