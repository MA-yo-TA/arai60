from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    # head is the first node, not the pointer to the first node.
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -100 <= Node.val <= 100 so ptr_to_head.val must be out of the range
        ptr_to_head = ListNode(200, head)
        cur = ptr_to_head

        while cur.next is not None and cur.next.next is not None:
            if cur.next.val == cur.next.next.val:
                # Want to find the last node of the duplication
                in_duplicate = cur.next
                while (
                    in_duplicate.next is not None
                    and in_duplicate.val == in_duplicate.next.val
                ):
                    in_duplicate = in_duplicate.next
                # Another duplication can start just after a duplication ends
                # So cur mustn't be update
                cur.next = in_duplicate.next

            else:
                cur = cur.next

        return ptr_to_head.next
