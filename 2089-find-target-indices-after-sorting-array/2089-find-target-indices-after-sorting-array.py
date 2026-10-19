class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
            if output and nums[i] != target:
                break

        return output