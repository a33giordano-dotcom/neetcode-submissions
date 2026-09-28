class Solution:
    def dfs(self, row, col, seen, grid) -> int:
        stack = [(row, col)]
        seen.add((row, col))
        area = 1  # Count the starting cell

        while stack:
            r, c = stack.pop()
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for rd, cd in neighbors:
                if rd < 0 or rd >= len(grid):
                    continue 
                if cd < 0 or cd >= len(grid[0]):
                    continue 
                if (rd, cd) in seen:
                    continue 
                if grid[rd][cd] == 1:
                    stack.append((rd, cd))
                    seen.add((rd, cd))
                    area += 1  # Count this part of the island
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    island_area = self.dfs(row, col, seen, grid)
                    largest = max(largest, island_area)
        return largest