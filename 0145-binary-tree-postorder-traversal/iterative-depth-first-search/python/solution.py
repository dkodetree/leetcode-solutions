# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]

        while stack:
           cur = stack.pop()
           if cur:
               result.append(cur.val)
               stack.append(cur.left)    # Push left first so that right sits on top and gets popped/processed first
               stack.append(cur.right)
        return result[::-1]          # Reverse to convert root-right-left into left-right-root (i.e. postorder)
