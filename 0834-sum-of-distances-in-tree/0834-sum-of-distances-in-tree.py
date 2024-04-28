class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Keep output and count of children arrays
        out = [0] * n
        count = [1] * n
        root = 0
        # Map parents and edges
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        # DFS function to fill count array
        def dfs(curr, parent, depth):
            nonlocal root
            o = 1
            for child in graph[curr]:
                if child != parent:
                    o += dfs(child, curr, depth + 1)
                    root += (depth + 1)
            count[curr] = o
            return o
        # Run dfs function
        dfs(0, -1, 0)
        # Second DFS function to find sum of dist for each node
        def dfs2(curr, parent, ans):
            out[curr] = ans
            for child in graph[curr]:
                if child != parent:
                    dfs2(child, curr, ans + (n - count[child]) - count[child])
        # Run second dfs function
        dfs2(0, -1, root)
        # Return output array
        return out