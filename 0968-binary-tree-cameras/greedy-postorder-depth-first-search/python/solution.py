# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # Status Constants
        HAS_CAM = 1     # node has a camera
        COVERED = 2     # node is covered (by child)
        NEEDS_COV = 3   # node is not covered

        cameras = 0     # camera counter

        # Greedy Postorder DFS
        def dfs(node) -> int:
            nonlocal cameras

            # Null nodes are automatically covered
            if not node:
                return COVERED

            # Postorder traversal- so process children first
            left_status = dfs(node.left)
            right_status = dfs(node.right)

            # If any child needs camera, then place camera at current node
            if left_status == NEEDS_COV or right_status == NEEDS_COV:
                cameras += 1
                return HAS_CAM

            # If any child has camera, then current node is already covered
            if left_status == HAS_CAM or right_status == HAS_CAM:
                return COVERED
            
            # Otherwise current node is not covered
            return NEEDS_COV
        
        return cameras + 1 if dfs(root) == NEEDS_COV else cameras
