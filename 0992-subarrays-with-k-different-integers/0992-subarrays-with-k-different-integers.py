class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, K):
            freq = {}
            left = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] not in freq or freq[nums[right]] == 0:
                    K -= 1
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while K < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        K += 1
                    left += 1
                
                count += (right - left + 1)
                
            return count

        return atMostK(nums, k) - atMostK(nums, k-1)



        # cnt = 0
        # for i in range(len(nums)):
        #     freq = {}
        #     for j in range(i, len(nums)):
        #         freq[nums[j]] = freq.get(nums[j] , 0) + 1
        #         if len(freq) == k:
        #             cnt += 1 
        # return cnt
