"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict = {}
        if node is None:
            return None
        queue = [node]

        list_nodes = []
        while queue:
            n = queue.pop()
            if n.val not in dict.keys():
                dict[n.val] = ([neighbor.val for neighbor in n.neighbors], Node(n.val))
                if n.neighbors is not None:
                    for neighbor in n.neighbors:
                        if neighbor.val not in dict.keys():

                            queue.append(neighbor)
        
        for key in dict:
            neighbors = [dict[val][1] for val in dict[key][0]]
            dict[key][1].neighbors = neighbors if neighbors is not None else []
        
        return dict[node.val][1]

        
