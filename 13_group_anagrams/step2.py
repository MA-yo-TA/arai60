from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord("a")] += 1

            groups[tuple(char_count)].append(string)

        return list(groups.values())
