from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    # head is the first node, not the pointer to the first node.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr_to_first_node = ListNode(200, head)
        cur = ptr_to_first_node
        while cur and cur.next and cur.next.next:
            while cur.next.val == cur.next.next.val:
                duplicate_val = cur.next.val
                while cur.next and cur.next.val == duplicate_val:
                    cur.next = cur.next.next
                if cur.next is None or cur.next.next is None:
                    break
            cur = cur.next
        return ptr_to_first_node.next
