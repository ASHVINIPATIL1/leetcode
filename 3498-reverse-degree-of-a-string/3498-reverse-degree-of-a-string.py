class Solution:
    def reverseDegree(self, s: str) -> int:
        r = 0

        for i in range(1, len(s) + 1):
            r += (i * (ord('z') - ord(s[i - 1])  + 1))
        return r