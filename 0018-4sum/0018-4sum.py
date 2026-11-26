class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if  j > i + 1 and nums[j] == nums[j-1]:
                    continue

                p = j + 1
                k = n - 1

                while p < k:
                    summ = nums[i] + nums[j] + nums[p] + nums[k]

                    if summ > target:
                        k -= 1

                    elif summ < target:
                        p += 1

                    else:
                        ans.append([nums[i], nums[j], nums[p], nums[k]])

                        p += 1
                        k -= 1

                        while p < k and nums[p] == nums[p-1]:
                            p += 1

                        while p < k and nums[k] == nums[k+1]:
                            k -= 1

        return ans