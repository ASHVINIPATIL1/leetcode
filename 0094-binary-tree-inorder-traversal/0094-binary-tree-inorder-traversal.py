# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        inorder = []
        stack = []
        node = root

        while True:
            if node != None: 
                stack.append(node)
                node = node.left
            else:
                if not len(stack):
                    break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right

        return inorder 