class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_r = 0
        sum_l = 0
        sum_max = 0

        # add all k elements from left(begining)
        # store maximum sum in variable
        for i in range(k):
            sum_l = sum_l + cardPoints[i]
            sum_max = max(sum_l, sum_max)
        
        # define start index of right(ending)
        r = len(cardPoints) - 1

        # run loop to substract element from sum_l and keep adding element from ending and decrement r -- keep track of max sum 
        for i in range(k - 1, -1, -1):
            sum_l = sum_l - cardPoints[i]    # substracting element from sum_l so we can keep the size of window as k
            sum_r = sum_r + cardPoints[r]    # add element to sum_r to compansate for the removal of element from sum_l
            r -= 1  
            sum_max = max(sum_max, sum_l+sum_r)   # keep max of max_sum and (sum_l + sum_r)

        return sum_max
