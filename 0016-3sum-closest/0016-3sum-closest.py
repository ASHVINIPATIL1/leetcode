class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            j = i + 1
            k = n-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if abs(summ - target) < abs(closest - target):
                    closest = summ
                if summ > target:
                    k -= 1
                elif summ < target:
                    j += 1
                else:
                    return summ
        return closest

