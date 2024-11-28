from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_prefix_sum = defaultdict(int)
        # Count the virtual prefix sum for the empty sub-array
        count_prefix_sum[0] = 1

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            count += count_prefix_sum[target]
            count_prefix_sum[prefix_sum] += 1

        return count
