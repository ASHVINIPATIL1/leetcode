class Solution:
    def findNSE(self, nums):
        n = len(nums)
        nse = [n] * n   # if there is no nse then default is n
        st = []

        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()

            if st:
                nse[i] = st[-1]

            st.append(i)

        return nse
    
    def findNGE(self, nums):
        n = len(nums)
        nge = [n] * n   # if there is no nge then default is n
        st = []

        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()

            if st:
                nge[i] = st[-1]
            
            st.append(i)
        
        return nge

    def findPSEE(slef, nums):
        n = len(nums)
        psee = [-1] * n   # if there is no psee then default is -1
        st = []

        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            
            if st:
                psee[i] = st[-1]

            st.append(i)

        return psee
    
    def findPGEE(self, nums):
        n = len(nums)
        pgee = [-1] * n  # if there is no pgee then default is -1
        st = []

        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            
            if st:
                pgee[i] = st[-1]
            
            st.append(i)
        
        return pgee

    # function to calculate min of subarray
    def SubarrayMins(self, nums):
        nse = self.findNSE(nums)
        psee = self.findPSEE(nums)

        n = len(nums)

        sumMins = 0

        for i in range(n):
            # count of possible left boundries
            left = i - psee[i]
            # count of possible right boundries
            right = nse[i] - i
            # count of subarrays where current ele is minimum
            freq = left * right
            # contribution of current ele
            val = freq * nums[i]

            sumMins += val
        
        return sumMins

    # function to calculate max of subarray
    def SubarrayMaxs(self, nums):
        nge = self.findNGE(nums)
        pgee = self.findPGEE(nums)

        n = len(nums)

        sumMaxs = 0

        for i in range(n):
            # count of possible left boundries
            left = i - pgee[i]
            # count of possible right boundries
            right = nge[i] - i
            # count of subarrays where current ele is minimum
            freq = left * right
            # contribution of current ele
            val = freq * nums[i]

            sumMaxs += val
        
        return sumMaxs

    def subArrayRanges(self, nums: list[int]) -> int:
        return self.SubarrayMaxs(nums) - self.SubarrayMins(nums)