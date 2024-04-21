class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Make an adjacency list
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # DFS function to traverse from source to destination
        def dfs(start, visited):
            if start == destination:
                return True
            visited.add(start)
            for adj in graph[start]:
                if adj not in visited:
                    if dfs(adj, visited):
                        return True
            return False
        # Run DFS with a visited set and return result
        visited = set()
        return dfs(source, visited)