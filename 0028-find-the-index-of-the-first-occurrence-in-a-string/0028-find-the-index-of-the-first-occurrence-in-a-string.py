class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if haystack in needle:
        #     return needle.index(haystack)

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1