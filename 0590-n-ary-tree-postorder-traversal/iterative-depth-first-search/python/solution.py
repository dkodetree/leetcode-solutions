"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.children:
                    # Push children left-to-right so rightmost child stays on top and pops first
                    stack.extend(node.children)
        return result[::-1] # Reverse to convert [Root -> Rightmost ... Leftmost] into [Leftmost ... Rightmost -> Root] (i.e. postorder)
