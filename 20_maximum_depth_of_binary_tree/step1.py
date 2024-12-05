from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes_to_visit: deque[tuple[TreeNode, int]] = deque([(root, 1)])

        while nodes_to_visit:
            node, depth = nodes_to_visit.popleft()
            if node.left:
                nodes_to_visit.append((node.left, depth + 1))
            if node.right:
                nodes_to_visit.append((node.right, depth + 1))

        return depth
