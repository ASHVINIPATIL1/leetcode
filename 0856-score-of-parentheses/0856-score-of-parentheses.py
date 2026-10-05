class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        st = [0]

        for i in range(n):
            if s[i] == '(':
                st.append(0)
            else:
                inside = st.pop()

                if inside == 0:
                    score = 1
                else:
                    score = 2 * inside
                
                st[-1] += score

        return st[0]