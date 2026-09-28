class Solution:
    
    def dfs(self, r, c, grid, visited):
        stack = [(r, c)]
        visited.add((r, c))
        while stack:
            row, col = stack.pop()
            neighbors = [(row + 1, col),(row - 1, col), (row, col + 1), (row, col - 1)]
            for rd, cd in neighbors:
                if rd < 0 or rd >= len(grid):
                    continue 
                if cd < 0 or cd >= len(grid[0]):
                    continue 
                if (rd, cd) in visited:
                    continue
                if grid[rd][cd] == '1':
                    stack.append((rd, cd))
                    visited.add((rd, cd))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    self.dfs(row, col, grid, visited)
                    islands += 1
        return islands
                
        

