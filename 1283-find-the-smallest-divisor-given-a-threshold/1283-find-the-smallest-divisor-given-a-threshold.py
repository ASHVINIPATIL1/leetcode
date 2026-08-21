class Solution:
    def div(self, nums, divisor):
        sumation = 0
        for num in nums:
            sumation += math.ceil(num / divisor)
        return sumation

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high) // 2

            if self.div(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low