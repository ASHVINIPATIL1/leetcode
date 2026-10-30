# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        inorderTree = []

        if root is None:
            return inorderTree

        inorderTree.extend(self.inorderTraversal(root.left))

        inorderTree.append(root.val)

        inorderTree.extend(self.inorderTraversal(root.right))

        return inorderTree