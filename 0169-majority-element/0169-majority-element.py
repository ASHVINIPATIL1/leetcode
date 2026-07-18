class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # n = len(nums)

        # freq = n // 2

        # hshArr = [0] * (100)

        # for i in range(n):
        #     hshArr[nums[i]] += 1
        
        # return hshArr.index(freq) + 1

        # time = O(n), space = O(n)
        # better than brute force

        n = len(nums)
        # sort
        nums = sorted(nums)
        freq = 1
        ans = nums[0]
        for i in range(1, n):
            if (nums[i] == nums[i-1]):
                freq += 1
            else:
                freq = 1
                ans = nums[i]
            if freq > (n//2):
                return ans
        return ans
        # time  = nlogn + n


            