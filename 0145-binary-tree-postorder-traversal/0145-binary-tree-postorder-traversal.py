# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        st1 = []
        st2 = []

        postorder = []

        if root is None:
            return postorder

        st1.append(root)

        while st1:
            root = st1.pop()
            st2.append(root)
            
            if root.left != None:
                st1.append(root.left)
                
            if root.right != None:
                st1.append(root.right)

        while st2:
            postorder.append(st2.pop().val)
        
        return postorder