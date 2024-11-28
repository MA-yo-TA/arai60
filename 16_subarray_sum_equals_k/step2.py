from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_prefix_sums: dict[int, int] = defaultdict(int)
        # The virtual prefix sum for the empty sub-array
        count_prefix_sums[0] = 1
        prefix_sum = 0
        count = 0
        # Calculate the sums of the sub-arrays beginning at the head of the array and ending at each index, which are called "prefix-sums".
        # And at the same time, count the number of the former prefix sums which meet the condition with the current one.
        for tail in range(len(nums)):
            prefix_sum += nums[tail]
            # The given condition is `current_prefix_sum - former_prefix_sum == k`, so it can be considered as below
            target = prefix_sum - k
            count += count_prefix_sums[target]
            count_prefix_sums[prefix_sum] += 1

        return count
