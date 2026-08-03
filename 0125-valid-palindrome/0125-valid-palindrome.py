import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower().replace(" ", "")
        s = re.sub(r'[^a-z0-9]', '', s)
 
        rev = s[::-1]

        if rev == s:
            return True
        else:
            return False