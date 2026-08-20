class Solution:
    def totalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        low, high = 1, max_pile
        ans = max_pile

        while low <= high:
            mid = (low + high) // 2

            totalH = self.totalHours(piles, mid)

            if totalH <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        
