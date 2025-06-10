# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = collections.deque([root])

        while queue:
            cur_level_res = []
            for _ in range(len(queue)):
                node = queue.popleft()

                # explore node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                cur_level_res.append(node.val)
            res.append(cur_level_res)
        return res
