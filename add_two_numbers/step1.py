from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        ans_head = ListNode()
        ans_ptr = ans_head
        carry = 0
        while cur1 is not None or cur2 is not None or carry == 1:
            if cur1 is None:
                cur1 = ListNode(0, None)
            if cur2 is None:
                cur2 = ListNode(0, None)

            # In addition, the carry is at most 1
            if cur1.val + cur2.val + carry >= 10:
                ans_ptr.next = ListNode(cur1.val + cur2.val + carry - 10)
                carry = 1
            else:
                ans_ptr.next = ListNode(cur1.val + cur2.val + carry)
                carry = 0

            cur1 = cur1.next
            cur2 = cur2.next
            ans_ptr = ans_ptr.next

        return ans_head.next
