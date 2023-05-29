# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # Only need 1 holder
        right_holder = root.right

        # Then we can override right
        root.right = invertTree(root.left) if root.left is not None else None
        root.left = invertTree(right_holder) if right_holder is not None else None

        return root

def main():
    s = Solution()
    input = TreeNode()
    print(s.invertTree(input));


if __name__ == "__main__":
    main()
