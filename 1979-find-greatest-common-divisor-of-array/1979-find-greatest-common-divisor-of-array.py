class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)

        while smallest != 0:
            largest , smallest = smallest ,largest % smallest
        return largest