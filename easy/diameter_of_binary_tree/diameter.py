# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diam = 0

    def diam(self, node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_diam = self.diam(node.left)
            right_diam = self.diam(node.right)
            new_diam = left_diam + right_diam
            if new_diam > self.max_diam:
                self.max_diam = new_diam
            return 1 + max(left_diam, right_diam)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam(root)

        return self.max_diam
