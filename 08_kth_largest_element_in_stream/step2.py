from typing import List


def left(parent: int) -> int:
    return 2 * parent + 1


def right(parent: int) -> int:
    return 2 * parent + 2


def parent(child: int) -> int:
    return (child + 1) // 2 - 1


def min_heapify(nums: List[int], i: int) -> List[int]:
    length = len(nums)
    smallest = i
    if left(i) < length and nums[i] > nums[left(i)]:
        smallest = left(i)

    if right(i) < length and nums[smallest] > nums[right(i)]:
        smallest = right(i)

    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        return min_heapify(nums, smallest)

    return nums


def build_min_heap(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1 // 2, -1, -1):
        nums = min_heapify(nums, i)
    return nums


def heap_extract_min(heap: List[int]) -> tuple[List[int], int]:
    min = heap[0]
    heap[0] = heap[-1]
    heap = heap[:-1]
    min_heapify(heap, 0)
    return (heap, min)


def min_heap_insert(heap: List[int], key: int) -> List[int]:
    i = len(heap)
    heap = heap + [key]
    while i > 0 and heap[i] < heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)
    return heap


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = build_min_heap(nums)
        while len(self.nums) > self.k:
            self.nums, _ = heap_extract_min(self.nums)

    def add(self, val: int) -> int:
        self.nums = min_heap_insert(self.nums, val)
        if len(self.nums) > self.k:
            self.nums, _ = heap_extract_min(self.nums)

        return self.nums[0]


def main():
    kl = KthLargest(3, [4, 5, 8, 2])
    print(kl.nums)
    print(kl.add(3), kl.nums)
    print(kl.add(5), kl.nums)
    print(kl.add(10), kl.nums)
    print(kl.add(9), kl.nums)
    print(kl.add(4), kl.nums)


if __name__ == "__main__":
    main()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
