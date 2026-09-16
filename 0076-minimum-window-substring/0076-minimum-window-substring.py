class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        required = {}
        window = {}

        for c in t:
            required[c] = required.get(c, 0) + 1

        matched = 0
        required_types = len(required)

        best = [-1, -1]
        best_len = float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in required and window[c] == required[c]:
                matched += 1
            
            while matched == required_types:
                if right - left + 1 < best_len:
                    best = [left, right]
                    best_len = right - left + 1

                c = s[left]
                window[c] -= 1

                if c in required and window[c] < required[c]:
                    matched -= 1
                
                left += 1

        l, r = best
        return s[l : r+1] if best_len != float('inf') else ""

        