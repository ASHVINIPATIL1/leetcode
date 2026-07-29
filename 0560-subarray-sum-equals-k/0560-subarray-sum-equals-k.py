class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count +=  1
        # return count 
        # O(n^2)

        mapp = {}
        mapp[0] = 1
        preSum = 0
        cnt = 0
        for i in range(len(nums)):
            preSum += nums[i]
            remove = preSum - k
            if remove in mapp:
                cnt += mapp[remove]
            mapp[preSum] = mapp.get(preSum, 0) + 1
            
        return cnt


         