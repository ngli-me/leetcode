# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head is not None:
            stack.insert(0, head)
            head = head.next

        if len(stack) == 0:
            return None

        new_head = stack[0]
        current_node = new_head
        for node in stack[1:]:
            node.next = None
            current_node.next = node
            current_node = current_node.next

        return new_head
