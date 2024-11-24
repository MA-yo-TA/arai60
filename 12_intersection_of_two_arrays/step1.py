from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection: List[int] = list(set(nums1) & set(nums2))

        return intersection
