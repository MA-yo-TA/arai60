from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.count_area_of_island(grid, 0, i, j)

                    if area > max:
                        max = area

        return max

    def count_area_of_island(self, grid, area, i, j):
        if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j or grid[i][j] != 1:
            return area

        area += 1
        grid[i][j] = -1

        area = self.count_area_of_island(grid, area, i - 1, j)
        area = self.count_area_of_island(grid, area, i + 1, j)
        area = self.count_area_of_island(grid, area, i, j - 1)
        area = self.count_area_of_island(grid, area, i, j + 1)

        return area
