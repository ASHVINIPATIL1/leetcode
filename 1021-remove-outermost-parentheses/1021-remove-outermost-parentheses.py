class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ''   # to keep the final output 
        st = []  
        start = 0   # indicates start of the primitive decomposition
        left = 0  # no of left parenthesis
        right = 0  # no of right parenthesis

        for i, c in enumerate(s):
            if c == '(': # append ( and increse counter of left 
                st.append(c) 
                left += 1
            elif c == ')': # append ) and increse counter of right 
                st.append(c)
                right += 1

            if left == right:  # if left == right that means it is a primitive decomposition eg - (()()) left = 3, right = 3
            
                output = output + s[start+1 : i]  # exclude the 1st and last bracket and concatinate the remaining string to output
                st = [] # empty the stack, left, right
                left = 0
                right = 0
                start = i+1 # since 1st primitive decomposition is done set start to i +

        return output  