class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = 0
        for i in range(1, n + 1):
            sumEven += 2*i

        sumOdd = 0
        for i in range(1, n + 1):
            sumOdd += 2*i - 1

        return math.gcd(sumEven, sumOdd)

