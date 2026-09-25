class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            n = str(n)
            summ = 0

            for digit in n:
                summ += int(digit) ** 2

            n = summ

        return True

            