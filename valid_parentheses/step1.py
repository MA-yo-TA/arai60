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
                if char == ")" and top == "(":
                    continue
                if char == "]" and top == "[":
                    continue
                if char == "}" and top == "{":
                    continue

                return False

        if stack:
            return False

        return True
