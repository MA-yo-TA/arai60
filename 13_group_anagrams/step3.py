from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            counter = [0] * 26
            for char in string:
                counter[ord(char) - ord("a")] += 1

            groups[tuple(counter)].append(string)

        return list(groups.values())
