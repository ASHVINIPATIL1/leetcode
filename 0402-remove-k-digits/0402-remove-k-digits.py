class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"

        st = []
        d = 0

        for c in num:
            while st and d < k and st[-1] > c:
                st.pop()
                d += 1
            st.append(c)

        while d < k:
            st.pop()
            d += 1
        
        ans = ("".join(st)).lstrip('0')

        return ans if ans else '0'