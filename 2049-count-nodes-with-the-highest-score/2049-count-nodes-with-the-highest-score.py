class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # Keep an output array that contains the max score and n nodes w max score
        out = [0, 1]
        # Keep an array of nodes and number of children
        n = len(parents)
        nodes = [[0, 0] for _ in parents]
        # Map parents as edges in a graph
        graph = defaultdict(list)
        for i in range(n):
            if parents[i] != -1:
                graph[parents[i]].append(i)
        # DFS to determine number of children at each node
        def dfs(node):
            if not graph[node]:
                return 1
            size = 1
            # If node has one child
            if len(graph[node]) >= 1:
                left_size = dfs(graph[node][0])
                nodes[node][0] = left_size
                size += left_size
            # If node has two children
            if len(graph[node]) >= 2:
                right_size = dfs(graph[node][1])
                nodes[node][1] = right_size
                size += right_size
            return size
        # Run dfs function to calculate each node's child count
        dfs(0)
        # For node in nodes, update output's max and n values
        for node in nodes:
            l, r = max(node[0], 1), max(node[1], 1)
            p = max(n - (node[0] + node[1]) - 1, 1)
            score =  l * r * p
            if score == out[0]:
                out[1] += 1
            if score > out[0]:
                out[0] = score
                out[1] = 1
        # Return output's n value
        return out[1]