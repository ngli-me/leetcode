# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None): return True
        elif (root.left == None and root.right == None):
            # Root is the only node
            return True
        check = self.check_subtree(root, 0)
        return check >= 0

    def check_subtree(self, root: Optional[TreeNode], height: int) -> int: # Returns height of two subtrees
        left = right = 0
        if root.left is not None:
            left = self.check_subtree(root.left, height + 1)
        if root.right is not None:
            right = self.check_subtree(root.right, height + 1)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

def main():
    s = Solution()
    input = TreeNode(1)
    print(s.isBalanced(input, 1, 1, 2));

if __name__ == "__main__":
    main()

