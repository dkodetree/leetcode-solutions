# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def find_paths(node, remaining_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining_sum: 
                res.append(path.copy())
            else:
                find_paths(node.left, remaining_sum - node.val) 
                find_paths(node.right, remaining_sum - node.val) 
            path.pop()     # Undo path change

        find_paths(root, targetSum)
        return res
