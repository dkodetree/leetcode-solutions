class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = collections.deque([root])

        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()

                # explore node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                current_level.append(node.val)

            res.append(current_level)
            
        return res
