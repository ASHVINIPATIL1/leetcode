class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(min(nums), max(nums) + 1) if i not in s]

        # x = min(nums)
        # y = max(nums)
        # missing = [0] * (y+1)
        # ans = []

        # for i in range(0, len(nums)):
        #     missing[nums[i]] += 1

        # for i in range(x, y+1):
        #     if missing[i] == 0:
        #         ans.append(i)
        # return ans
