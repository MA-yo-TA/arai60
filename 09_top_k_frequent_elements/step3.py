from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        freqs: List[tuple[int, int]] = [(freq, num) for num, freq in counter.items()]
        heapq.heapify(freqs)

        while len(freqs) > k:
            heapq.heappop(freqs)

        return [freq[1] for freq in freqs]
