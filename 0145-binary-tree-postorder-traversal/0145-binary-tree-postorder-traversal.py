# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        st = []
        postorder = []

        curr = root

        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left

            else:
                temp = st[-1].right

                if temp is None:
                    temp = st.pop()
                    postorder.append(temp.val)

                    while st and temp == st[-1].right:
                        temp = st.pop()
                        postorder.append(temp.val)

                else:
                    curr = temp

        return postorder