# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []

        if root is None:
            return result

        nodesQueue = deque()
        nodesQueue.append(root)

        lefttoright = True

        while nodesQueue:
            size = len(nodesQueue)
            row = [0] * size

            for i in range(size):
                node = nodesQueue.popleft()

                index = i if lefttoright else size-1-i

                row[index] = node.val

                if node.left:
                    nodesQueue.append(node.left)

                if node.right:
                    nodesQueue.append(node.right)

            lefttoright = not lefttoright

            result.append(row)

        return result