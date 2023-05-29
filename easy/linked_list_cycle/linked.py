# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Anything that terminates the linked list means it cannot loop
        visited = {}

        while head:
            if head not in visited.keys():
                visited[head] = 1
            else:
                # We already visited, so we hit a loop
                return True
            head = head.next
        return False

def main():
    s = Solution()

if __name__ == "__main__":
    main()

