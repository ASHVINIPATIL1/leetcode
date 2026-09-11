class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26

        left = 0
        maxCount = 0  #most freq char in current window
        maxLength = 0

        for right in range(n):
            freq[ord(s[right]) - ord('A')] += 1
            maxCount = max(maxCount, freq[ord(s[right]) - ord('A')])

            # if current windoe needs more than k replacement 
            while (right - left + 1) - maxCount > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength