class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        i = len(s) - 1
        while s[i] != " " and i >= 0:
            if s[i].isalpha():
                length += 1
                i -= 1
        return length