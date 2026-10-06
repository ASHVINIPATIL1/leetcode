class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []

        for i in range(len(s)):

            if st and (st[-1] == '(' and s[i] == ')'):
                st.pop()
            else:
                st.append(s[i])

        return len(st)
