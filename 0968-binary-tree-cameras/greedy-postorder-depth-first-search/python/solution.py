# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # Status Constants
        NEEDS_CAM = 0   # node is not covered
        COVERED = 1     # node is covered (by child)
        HAS_CAM = 2     # node has a camera

        cameras = 0  # camera counter

        # Greedy Post order DFS
        def dfs(node) -> int:
            nonlocal cameras

            # Null nodes are automatically covered
            if not node:
                return COVERED

            # Post-order traversal- so process children first
            left_status = dfs(node.left)
            right_status = dfs(node.right)

            # If any child needs a camera, then place camera at this node
            if left_status == NEEDS_CAM or right_status == NEEDS_CAM:
                cameras += 1
                return HAS_CAM

            # If any child has a camera, then this node is already covered
            if left_status == HAS_CAM or right_status == HAS_CAM:
                return COVERED
            
            # Otherwise, node is not covered
            return NEEDS_CAM
        
        return cameras + 1 if dfs(root) == NEEDS_CAM else cameras
