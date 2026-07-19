class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        hashArr = [0] * (n + 1)

        for i in range(n):
            hashArr[nums[i]] += 1

        for h in hashArr:
            if h > 1:
                return hashArr.index(h)

