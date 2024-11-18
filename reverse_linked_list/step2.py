from typing import Optional
from collections import deque


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
        stack: deque = deque()

        while cur is not None:
            stack.append(cur.val)
            cur = cur.next

        prev = dummy_head
        while len(stack) > 0:
            val = stack.pop()
            prev.next = ListNode(val)
            prev = prev.next

        return dummy_head.next
