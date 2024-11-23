from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2ind: dict[int, List[int]] = {}

        for i in range(len(nums)):
            num2ind[nums[i]] = num2ind.get(nums[i], []) + [i]

        for i1 in range(len(nums)):
            complement = target - nums[i1]
            if indices := num2ind.get(complement):
                # Can't use the same element twice
                if indices != [i1]:
                    # take the last one because the first one in the list is tested first if the same numbers exist.
                    # Can return here because it is assumed that each input has exactly one solution
                    return [i1, indices[-1]]

        # would not come here because each input has exactly one solution
        return []
