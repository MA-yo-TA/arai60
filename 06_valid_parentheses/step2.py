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
                if self.is_pair(char, top):
                    continue

                return False

        if stack:
            return False

        return True

    def is_pair(self, char, top):
        if (
            (char == ")" and top == "(")
            or (char == "]" and top == "[")
            or (char == "}" and top == "{")
        ):
            return True
        else:
            return False
