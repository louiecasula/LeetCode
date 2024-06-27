class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = []
        for e in edges:
            for n in e:
                if n in nodes:
                    return n
                nodes.append(n)