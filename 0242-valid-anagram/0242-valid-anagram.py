class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = [0] * 27
        t_hash = [0] * 27

        for c in s:
            s_hash[ord(c) - ord('a')] += 1

        for c in t:
            t_hash[ord(c) - ord('a')] += 1

        return s_hash == t_hash