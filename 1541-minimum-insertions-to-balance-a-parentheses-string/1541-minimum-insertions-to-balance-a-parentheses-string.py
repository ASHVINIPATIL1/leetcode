class Solution:
    def minInsertions(self, s: str) -> int:
        need = 0
        insertion = 0

        for c in s:
            if c == '(':
                need += 2

                if need % 2 == 1:
                    need -= 1
                    insertion += 1

            else:
                need -= 1

                if need < 0:
                    insertion += 1
                    need = 1
            
        return need + insertion