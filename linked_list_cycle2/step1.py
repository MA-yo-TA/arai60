from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 愚直にやるならこうだが、遅い。多分時間計算量が O(n^2)でメモリ計算量はO(n)
        visited: list[ListNode] = []
        current: Optional[ListNode] = head

        while current is not None:
            if current in visited:
                return current

            visited += [current]

            current = current.next

        return None
