from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum2indices = defaultdict(list)
        prefix_sums = [0] * (len(nums) + 1)
        # Calculate the sums of the sub-arrays beginning at the head and ending at each index.
        for end in range(len(nums)):
            prefix_sums[end + 1] = prefix_sums[end] + nums[end]
            prefix_sum2indices[prefix_sums[end + 1]].append(end)

        count = 0
        # for all sub-arrays, their sums are able to be calculated with two sums of sub-arrays beginning at the head of the parent array
        # e.g. the sum of a sub-array beginning at 2 in index and ending at 4 in index is `sum[beginning at 0, ending at 4] - sum[beginning at 0, ending at 2]`
        for end in range(len(nums)):
            if prefix_sums[end + 1] == k:
                count += 1

            target = prefix_sums[end + 1] - k
            if candidates := prefix_sum2indices[target]:
                count += len([ind for ind in candidates if ind < end])

        return count
