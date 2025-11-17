# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_cnt = collections.defaultdict(int)
        prefix_sum_cnt[0] = 1   # Base case: empty path sum

        def dfs(node, cur_sum):
            if not node:
                return 0

            cur_sum += node.val
            count = prefix_sum_cnt[cur_sum - targetSum]  # Paths ending here where prev_sum = cur_sum - targetSum

            prefix_sum_cnt[cur_sum] += 1    # Add current prefix sum to the map
            count += dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
            prefix_sum_cnt[cur_sum] -= 1    # Remove current prefix sum before returning
            return count

        return dfs(root, 0)
