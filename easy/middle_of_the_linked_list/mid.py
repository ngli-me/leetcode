# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        current = head

        while current:
            current = current.next
            if current is None:
                return mid

            current = current.next
            mid = mid.next
        return mid
