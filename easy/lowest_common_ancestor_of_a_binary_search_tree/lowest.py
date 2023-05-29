# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # maybe keep track of traversed nodes for ancestors of each, then just have to go back and grab the last common one
        # ig dont need to keep track of both just shared ones
        ancestors = [root]

        position_p = root
        position_q = root
        while position_p and position_q:
            if position_p.val > p.val:
                # check left side
                position_p = position_p.left
            elif position_p.val < p.val:
                # check right side
                position_p = position_p.right
            else:
                # found p, stop?
                position_p = None

            if position_q.val > q.val:

                # check left side
                position_q = position_q.left
            elif position_q.val < q.val:
                # check right side
                position_q = position_q.right
            else:
                # found q, stop?
                position_q = None

            if position_p is position_q and position_p is not None:
                ancestors.append(position_q) # might shallow copy double check

        return ancestors.pop()

def main():
    s = Solution()
    input = TreeNode(1)
    print(s.lowestCommonAncestor(input, 1, 1, 2));

if __name__ == "__main__":
    main()

