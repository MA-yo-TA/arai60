from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.count_area_of_island(grid, i, j)
                    max_area = max(area, max_area)
        return max_area

    def count_area_of_island(self, grid, i, j):
        if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j or grid[i][j] != 1:
            return 0

        grid[i][j] = -1

        return (
            1
            + self.count_area_of_island(grid, i - 1, j)
            + self.count_area_of_island(grid, i + 1, j)
            + self.count_area_of_island(grid, i, j - 1)
            + self.count_area_of_island(grid, i, j + 1)
        )
