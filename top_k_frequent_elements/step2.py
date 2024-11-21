from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 速くなった O(n)
        counter = Counter(nums)

        # List of (frequency, val)
        # frequency の大小でタプルの大小比較が決まるのでこれをヒープにするとルートが頻度最小になる
        freqs: List[tuple[int, int]] = [(freq, num) for num, freq in counter.items()]

        heapq.heapify(freqs)
        while len(freqs) > k:
            heapq.heappop(freqs)

        return [item[1] for item in freqs]
