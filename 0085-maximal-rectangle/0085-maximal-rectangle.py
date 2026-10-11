class Solution:
    def maxInHistogram(self, arr):
        maxi = 0
        st = []
        arr.append(0)

        for i in range(len(arr)):

            while st and arr[st[-1]] >= arr[i]:

                height = arr[st.pop()]
                width = i if not st else i - st[-1] - 1
                maxi = max(maxi, height * width)
            
            st.append(i)

        return maxi


    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        r = len(matrix)
        if r == 0:
            return 0
        c = len(matrix[0])

        ps = [0] * c
        maxArea = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    ps[j] += 1
                else:
                    ps[j] = 0
            
            maxArea = max(maxArea, self.maxInHistogram(ps.copy()))
        
        return maxArea