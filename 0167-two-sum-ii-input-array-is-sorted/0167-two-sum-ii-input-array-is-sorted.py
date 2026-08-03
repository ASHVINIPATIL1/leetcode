class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        summ = 0

        i = 0
        j = n -1

        while i < j:
            summ = numbers[i] + numbers[j]
            if summ > target:
                j -= 1
            elif summ < target:
                i += 1
            else:
                return [i+1, j+1]

        