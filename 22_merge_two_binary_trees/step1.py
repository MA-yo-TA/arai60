from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        return self.merge_nodes(root1, root2)

    def merge_nodes(
        self, node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not node1:
            return node2
        if not node2:
            return node1

        return TreeNode(
            val=(node1.val + node2.val),
            left=self.merge_nodes(node1.left, node2.left),
            right=self.merge_nodes(node1.right, node2.right),
        )
