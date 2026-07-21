class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])

        num = int(num) + 1
        op = []
        
        for ch in str(num):
            op.append(int(ch))
        return op


            
