from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodes_to_visit = deque([(root, 1)])

        while nodes_to_visit:
            node, depth = nodes_to_visit.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                nodes_to_visit.append((node.left, depth + 1))
            if node.right:
                nodes_to_visit.append((node.right, depth + 1))

        return 0

        # もし DFS でやるなら↓だが、最短経路を求めるのは普通 BFS（全部のノードを見なくていい可能性が高い。DFS は全部のノードを見ないといけない。）
        # if not root:
        #     return 0
        # if root.left and root.right:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # elif root.left:
        #     return self.minDepth(root.left) + 1
        # elif root.right:
        #     return self.minDepth(root.right) + 1
        # else:
        #     return 1
