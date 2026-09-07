class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        existing = set()
        max_len = 0
        l_ptr = 0

        for r_ptr in range(n):
            while s[r_ptr] in existing:
                existing.remove(s[l_ptr])
                l_ptr += 1
            existing.add(s[r_ptr])

            max_len = max((r_ptr - l_ptr + 1), max_len)

        return max_len
