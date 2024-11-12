# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        fast = head
        slow = head

        while fast is not None:
            if fast.next is None:
                return False

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
