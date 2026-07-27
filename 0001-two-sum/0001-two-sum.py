class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            moreneeded = target - num
            if moreneeded in hashmap:
                return [hashmap[moreneeded],i]
            hashmap[num] = i
        return [-1, -1]