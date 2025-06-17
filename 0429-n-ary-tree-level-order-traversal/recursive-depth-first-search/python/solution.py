"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                dfs(child, level + 1)

        dfs(root, 0)
        return res
