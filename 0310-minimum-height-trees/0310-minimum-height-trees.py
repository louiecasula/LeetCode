class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edgecase: n == 1
        if n == 1:
            return [0]
        # Make an adjacency list
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        # Keep an edge count dict and a leaf node stack
        edge_count = {}
        leaves = deque()
        for nd, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(nd)
            edge_count[nd] = len(neighbors)
        # While there are leaf nodes, remove them
        while leaves:
            # If there are 2 or less nodes left, return them
            if n <= 2:
                return list(leaves)
            # Shift leaf node array, decrement n, update its neighbors' edge counts, add any new leaf nodes
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)