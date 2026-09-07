class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            hashm= [0] * (256)

            for j in range(i, n):
                if hashm[ord(s[j])] == 1:
                    break
                len_cur = j - i + 1

                max_len = max(len_cur, max_len)
                hashm[ord(s[j])] = 1  

        return max_len