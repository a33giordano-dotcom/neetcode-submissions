class Solution:

    def dfs(self, row, col, seen, grid):
        stack = [(row, col)]
        seen.add((row, col))
        while stack:
            r,c = stack.pop()
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c -1]]
            for rd, cd in neighbors:
                if rd < 0 or rd >= len(grid):
                    continue
                if cd < 0 or cd >= len(grid[0]):
                    continue 
                if (rd, cd) in seen:
                    continue 
                if grid[rd][cd] == '1':
                    stack.append((rd, cd))
                    seen.add((rd, cd))
    
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        seen = set()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in seen:
                    self.dfs(row, col, seen, grid)
                    islands += 1 
        return islands 

                
        

