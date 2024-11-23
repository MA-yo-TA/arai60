from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack: deque = deque()

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if not self.is_pair(top, char):
                    return False

        if stack:
            return False

        return True

    def is_pair(self, open: str, close: str) -> bool:
        if (
            (open == "(" and close == ")")
            or (open == "[" and close == "]")
            or (open == "{" and close == "}")
        ):
            return True
        else:
            return False
