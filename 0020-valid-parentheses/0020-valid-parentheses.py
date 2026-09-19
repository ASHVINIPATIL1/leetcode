class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] == '(' and ch == ')' or stack[-1] == '[' and ch == ']' or stack[-1] == '{' and ch == '}':
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0

        # stack = []

        # pairs = {
        #     ')':'(',
        #     ']':'[',
        #     '}':'{'
        # }
        # for ch in s:

        #     if ch in '([{':
        #         stack.append(ch)
        #     else:
        #         if not stack:
        #             return False
        #         if stack[-1] != pairs[ch]:
        #             return False
        #         stack.pop()
        # return len(stack) == 0