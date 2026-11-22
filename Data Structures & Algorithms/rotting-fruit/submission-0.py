class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        visited = set()
        q = deque()
        fresh = 0


        def rot(r,c):
            nonlocal fresh 
            if r >= rows or r < 0 or c >= cols or c < 0:
                return 
            if (r,c) in visited or grid[r][c] != 1:
                return 
            
            if grid[r][c] == 1:
                fresh -= 1

            visited.add((r,c))
            grid[r][c] = 2
            q.append([r,c])

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                nr, nc = q.popleft()
                rot(nr + 1, nc)
                rot(nr - 1, nc)
                rot(nr, nc + 1)
                rot(nr, nc - 1)
            minutes += 1
        
        return minutes if fresh == 0 else -1
