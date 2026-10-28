# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        postorderTree = []

        if root is None:
            return postorderTree

        postorderTree.extend(self.postorderTraversal(root.left))

        postorderTree.extend(self.postorderTraversal(root.right))

        postorderTree.append(root.val)

        return postorderTree