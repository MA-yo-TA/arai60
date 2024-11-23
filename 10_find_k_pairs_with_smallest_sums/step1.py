from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:

        sums: List[tuple[int, List[int]]] = []
        for i1 in range(min(k, len(nums1))):
            heapq.heappush(sums, (nums1[i1] + nums2[0], [i1, 0]))

        ans: List[List[int]] = []
        for i in range(k):
            indices = heapq.heappop(sums)[1]
            ans.append([nums1[indices[0]], nums2[indices[1]]])
            if indices[1] + 1 < len(nums2):
                heapq.heappush(
                    sums,
                    (
                        nums1[indices[0]] + nums2[indices[1] + 1],
                        [indices[0], indices[1] + 1],
                    ),
                )

        return ans
