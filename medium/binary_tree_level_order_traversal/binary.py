# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # append node, queue node to append children

        if root is None:
            return []
        else:
            ret = []
            queue = [[root, 0]]
            while queue:
                q = queue.pop()
                self.traverse(q[0], ret, queue, q[1])
            return ret

    def traverse(self, root: Optional[TreeNode], ret: List[List[int]], queue, height: int):
        if root is None:
            return

        if height + 1 > len(ret):
            ret.append([])

        ret[height].append(root.val)
        queue.append([root.right, height + 1])
        queue.append([root.left, height + 1])
