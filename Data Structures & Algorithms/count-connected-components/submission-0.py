class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for edge in edges:
            a,b = edge 
            adj[a].append(b)
            adj[b].append(a) 
        
        visited = set()

        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for j in adj[i]:
                dfs(j)
        
        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1 
        return components


