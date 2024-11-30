from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.mark_connected_land(grid, i, j)
                    count += 1

        return count

    def mark_connected_land(self, grid, i, j):
        if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j or grid[i][j] != "1":
            return

        grid[i][j] = "#"
        self.mark_connected_land(grid, i - 1, j)
        self.mark_connected_land(grid, i + 1, j)
        self.mark_connected_land(grid, i, j - 1)
        self.mark_connected_land(grid, i, j + 1)
