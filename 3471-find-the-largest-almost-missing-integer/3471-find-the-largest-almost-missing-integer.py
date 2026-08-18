class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarr = []
        for i in range(len(nums) - k + 1):
            subarr.append(nums[i : i+k])
        
        freq = {}

        for suba in subarr:
            for num in set(suba):
                freq[num] = freq.get(num, 0) + 1
        
        ans = max((num for num in freq if freq[num] == 1), default = -1)

        return ans
