from typing import List, NamedTuple
from collections import Counter


class CharCount(NamedTuple):
    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0
    e: int = 0
    f: int = 0
    g: int = 0
    h: int = 0
    i: int = 0
    j: int = 0
    k: int = 0
    l: int = 0
    m: int = 0
    n: int = 0
    o: int = 0
    p: int = 0
    q: int = 0
    r: int = 0
    s: int = 0
    t: int = 0
    u: int = 0
    v: int = 0
    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_counts: dict[CharCount, List[str]] = {}

        for cur_str in strs:
            char_count = CharCount(**Counter(cur_str))
            char_counts[char_count] = char_counts.get(char_count, []) + [cur_str]

        return [group for group in char_counts.values()]
