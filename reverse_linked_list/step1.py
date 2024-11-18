from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        dummy_head = ListNode()

        while cur is not None:
            if dummy_head.next is None:
                dummy_head.next = ListNode(cur.val)
            else:
                dummy_head.next = ListNode(cur.val, dummy_head.next)

            cur = cur.next

        return dummy_head.next
