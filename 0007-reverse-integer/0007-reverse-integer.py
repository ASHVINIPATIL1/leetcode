class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        result = 0
        sign = 0
        
        if x[0] == '-':
            sign = -1
            x = x[1:]
        else:
            sign = 1

        result = x[::-1]
        return sign * int(result) if (-2**31) <= int(result) <= (2**31) - 1 else 0 

