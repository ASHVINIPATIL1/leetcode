class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = len(grid)
        hashArr = [0] * ((l*l) + 1)
        for i in range(l):
            for j in range(l):
                hashArr[grid[i][j]] += 1
        hashArr = hashArr[1:]
        repeat = hashArr.index(2) + 1
        missing = hashArr.index(0) + 1
        return [repeat, missing]