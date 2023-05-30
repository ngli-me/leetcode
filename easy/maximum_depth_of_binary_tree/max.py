# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root, 1)

    def height(self, node: Optional[TreeNode], height) -> int:
            if node is None:
                return 0
            left_height = self.height(node.left, height + 1)
            right_height = self.height(node.right, height + 1)
            return max(left_height, right_height, height)
