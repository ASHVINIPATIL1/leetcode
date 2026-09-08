class Solution:
    def countCommas(self, n: int) -> int:
        c = 0
        if n >= 1000:
            for i in range(1000, n+1):
                if n >= 1000:
                    c += 1
            return c

        else:
            return 0