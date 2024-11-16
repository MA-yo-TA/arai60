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
        ans_dummy_head = ListNode()
        cur_ans = ans_dummy_head
        carry = 0
        while cur1 is not None or cur2 is not None or carry != 0:
            if cur1 is None:
                cur1 = ListNode(0, None)
            if cur2 is None:
                cur2 = ListNode(0, None)

            digit_sum = cur1.val + cur2.val + carry
            ans_digit = digit_sum % 10
            carry = digit_sum // 10
            cur_ans.next = ListNode(ans_digit)

            cur1 = cur1.next
            cur2 = cur2.next
            cur_ans = cur_ans.next

        return ans_dummy_head.next
