class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq = [0] * 128

        for ch in t:
            freq[ord(ch)] += 1

        left = 0
        count = 0
        start = 0
        min_len = float('inf')

        for right in range(len(s)):
            if freq[ord(s[right])] > 0:
                count += 1

            freq[ord(s[right])] -= 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                freq[ord(s[left])] += 1

                if freq[ord(s[left])] > 0:
                    count -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]