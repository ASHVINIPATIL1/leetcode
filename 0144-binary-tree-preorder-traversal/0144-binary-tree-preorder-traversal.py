# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        preorderTree = []

        if root == None:
            return preorderTree

        preorderTree.append(root.val)

        preorderTree.extend(self.preorderTraversal(root.left))
        preorderTree.extend(self.preorderTraversal(root.right))

        return preorderTree