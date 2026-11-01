# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # if root is None:
        #     return 0

        # queue = deque([root])
        # depth = 0

        # while queue:
        #     depth += 1
        #     level_size = len(queue)

        #     for i in range(level_size):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)
        
        # return depth

        if root is None:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh, rh)