class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        st = []
        maxArea = 0

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                element = st.pop()
                # st.pop()
                nse = i

                if st:
                    pse = st[-1]
                else:
                    pse = -1

                maxArea = max(maxArea, heights[element] * (nse - pse - 1))

            st.append(i)

        while st:
            nse = n
            element = st.pop()

            if st:
                pse = st[-1]
            else:
                pse = -1

            maxArea = max(maxArea, heights[element] * (nse - pse - 1))
    
        return maxArea