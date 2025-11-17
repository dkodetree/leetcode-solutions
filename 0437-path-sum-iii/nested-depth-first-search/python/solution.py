# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def count_paths_from(node, target):
            if not node:
                return 0
            paths_from_left_child = count_paths_from(node.left, target - node.val)
            paths_from_right_child = count_paths_from(node.right,  target - node.val)
            return (node.val == target) + paths_from_left_child + paths_from_right_child

        return count_paths_from(root, targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right, targetSum)
