class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        l = 0
        existing = set()

        for r in range(n):
            while s[r] in existing:
                existing.remove(s[l])
                l += 1
            existing.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len

