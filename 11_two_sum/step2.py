from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2ind: dict[int, List[int]] = {}

        for i in range(len(nums)):
            num2ind[nums[i]] = num2ind.get(nums[i], []) + [i]

        for i1 in range(len(nums)):
            complement = target - nums[i1]

            if indices := num2ind.get(complement):
                # 同じ index を2回使うことはできない
                if indices != [i1]:
                    # 同じ数だった場合はループでは前から順に試されるので、後ろを取る
                    i2 = indices[-1]
                    return [i1, i2]

        # You may assume that each input would have exactly one solution
        # なのでここには来ないはず
        return []
