import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd = math.gcd(min(nums), max(nums))
        return gcd