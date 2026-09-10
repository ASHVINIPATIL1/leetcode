class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        r = 0
        l = 0
        freq = [0] * 3

        for r in range(n):
            freq[ord(s[r])- ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                count += n-r
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1 

        return count