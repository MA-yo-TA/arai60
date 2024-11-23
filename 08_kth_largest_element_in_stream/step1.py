from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k - 1
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        if len(self.nums) == 0 or val >= self.nums[0]:
            self.nums = [val] + self.nums
        elif val >= self.nums[-1]:
            for i in range(1, len(self.nums)):
                if val >= self.nums[i]:
                    self.nums = self.nums[:i] + [val] + self.nums[i:]
                    break
        else:
            self.nums = self.nums + [val]

        return self.nums[self.target]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
