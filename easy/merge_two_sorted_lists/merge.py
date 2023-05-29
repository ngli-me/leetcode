from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Runtime is O(m+n)? have to iterate through both lists
        # Doesn't say, but looks like both lists are sorted by default
        combined_list = ListNode()
        current = combined_list
        while list1 and list2:
            if list1.val <= list2.val:
                print('l1', list1.val)
                current.next = ListNode(list1.val)
                current = current.next
                list1 = list1.next
            else:
                print('l2', list2.val)
                current.next = ListNode(list2.val)
                current = current.next
                list2 = list2.next

        # stitch on the remainder [marker:] to the combined list from the longer one
        if list1:
            print('l1 end')
            current.next = list1
        elif list2:
            print('l2 end', list2.val)
            current.next = list2 
        # remove the temporary first node
        combined_list = combined_list.next
        return combined_list

def main():
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    list1 = None
    list2 = ListNode(0)
    
    r = s.mergeTwoLists(list1, list2)
    print("checking")
    while r:
        print(r.val)
        r = r.next

if __name__ == "__main__":
    main()

