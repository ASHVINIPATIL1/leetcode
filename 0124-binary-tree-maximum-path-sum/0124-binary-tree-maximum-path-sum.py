# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        maxValue = [float('-inf')]

        def maxPathDown(node):
            if node is None: 
                return 0

            left = max(0, maxPathDown(node.left)) 
            right = max(0, maxPathDown(node.right)) 

            maxValue[0] = max(maxValue[0], left+right+node.val)

            return max(left, right) + node.val

        maxPathDown(root)
        return maxValue[0]

       