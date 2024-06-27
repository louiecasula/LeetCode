class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = []
        for e in edges:
            if e[0] in nodes:
                return e[0]
            nodes.append(e[0])
            if e[1] in nodes:
                return e[1]
            nodes.append(e[1])