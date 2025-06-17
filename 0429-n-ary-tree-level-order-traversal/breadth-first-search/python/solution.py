"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_res.append(node.val)
                queue.extend(node.children)
            result.append(level_res)
        
        return result
