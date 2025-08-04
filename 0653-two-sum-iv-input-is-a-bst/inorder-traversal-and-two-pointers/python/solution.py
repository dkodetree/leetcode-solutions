# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_values.append(node.val)
            inorder(node.right)
        
        inorder(root)

        left, right = 0, len(sorted_values) - 1
        while left < right:
            two_sum = sorted_values[left] + sorted_values[right]
            if two_sum == k:
                return True
            elif two_sum < k:
                left += 1
            else:
                right -= 1
        return False
