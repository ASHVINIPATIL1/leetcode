class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        ans = []

        for i in range(n):
            if len(ans) == 0 or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans