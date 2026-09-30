class Solution:
    def pse(self, arr: list[int]):
        n = len(arr)
        previousLess = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                previousLess[i] = stack[-1]

            stack.append(i)

        return previousLess

    def nsee(self, arr: list[int]):
        n = len(arr)
        nextLess = [n] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                nextLess[i] = stack[-1]

            stack.append(i)

        return nextLess

    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7

        previousLess = self.pse(arr)
        nextLess = self.nsee(arr)

        answer = 0

        for i in range(n):
            left = i - previousLess[i]
            right = nextLess[i] - i

            contribution = (arr[i] * left * right) % mod

            answer = (answer + contribution) % mod

        return answer