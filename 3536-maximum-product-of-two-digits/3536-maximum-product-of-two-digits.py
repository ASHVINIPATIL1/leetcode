class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        maxm = 0
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                prod = int(n[i]) * int(n[j])
                if prod > maxm:
                    maxm = prod
        return maxm
