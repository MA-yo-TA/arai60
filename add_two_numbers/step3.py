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
        dummy_head_ans = ListNode()
        cur_ans = dummy_head_ans
        carry = 0

        while cur1 is not None or cur2 is not None or carry != 0:
            if cur1 is None:
                cur1 = ListNode(0)
            if cur2 is None:
                cur2 = ListNode(0)

            sum = cur1.val + cur2.val + carry
            digit = sum % 10
            carry = sum // 10

            cur_ans.next = ListNode(digit)

            cur1 = cur1.next
            cur2 = cur2.next
            cur_ans = cur_ans.next

        return dummy_head_ans.next
