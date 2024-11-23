from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        class Pair:
            def __init__(self, i1, i2) -> None:
                self.i1 = i1
                self.i2 = i2
                self.num1 = nums1[i1]
                self.num2 = nums2[i2]
                self.sum = nums1[i1] + nums2[i2]

            def __eq__(self, other) -> bool:
                return self.sum == other.sum

            def __lt__(self, other) -> bool:
                return self.sum < other.sum

        pairs: List[Pair] = []
        for i1 in range(min(k, len(nums1))):
            heapq.heappush(pairs, Pair(i1, 0))

        ans: List[List[int]] = []
        for i in range(k):
            smallest_pair = heapq.heappop(pairs)
            ans.append([smallest_pair.num1, smallest_pair.num2])
            if smallest_pair.i2 + 1 < len(nums2):
                heapq.heappush(
                    pairs,
                    Pair(smallest_pair.i1, smallest_pair.i2 + 1),
                )

        return ans
