class Solution:
    def firstUniqChar(self, s: str) -> int:
        appeared = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in appeared:
                appeared[s[i]] = i
            elif appeared[s[i]] >= 0:
                appeared[s[i]] = -1
        candidate = [ind for ind in appeared.values() if ind >= 0]

        if candidate:
            return min(candidate)
        else:
            return -1
