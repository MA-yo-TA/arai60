from typing import List
import heapq
from functools import total_ordering


@total_ordering
class Frequency:
    def __init__(self, val: int, freq: int = 0) -> None:
        self.val = val
        self.freq = freq

    def __eq__(self, other) -> bool:
        return self.freq == other.freq

    def __lt__(self, other) -> bool:
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_uniq = set(nums)
        freqs: List[Frequency] = []
        # ここが遅い O(n^2)
        for num in nums_uniq:
            freqs.append(Frequency(num, nums.count(num)))

        heapq.heapify(freqs)
        while len(freqs) > k:
            heapq.heappop(freqs)

        return [item.val for item in freqs]
