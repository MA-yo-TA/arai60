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
            if cur.next.val == cur.next.next.val:
                # 重複の最後のノードを見つけて、そいつの次を cur.next にする
                # そこからさらに重複が始まるかもしれないので、cur は更新しない
                in_duplicate = cur.next
                while in_duplicate.next and in_duplicate.val == in_duplicate.next.val:
                    in_duplicate = in_duplicate.next
                cur.next = in_duplicate.next
            else:
                cur = cur.next
        return ptr_to_first_node.next
