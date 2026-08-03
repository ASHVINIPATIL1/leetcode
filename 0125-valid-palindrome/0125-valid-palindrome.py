import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = re.sub(r'[^a-z0-9]', '', s)
        n = len(s)
        
        left = 0
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True