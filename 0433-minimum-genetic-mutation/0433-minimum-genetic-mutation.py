class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Edgecase: endGene not in bank
        if endGene not in bank:
            return -1
        # Keep a stack and a visited set for BFS
        stack = []
        stack.append((startGene, 0))
        visited = {startGene}
        # While the stack isn't empty,
        while len(stack) > 0:
            # If the shifted gene is the end, return it's level
            current = stack.pop(0)
            if current[0] == endGene:
                return current[1]
            # Else, check all possible mutations
            for i in range(len(current[0])):
                for letter in 'ACGT':
                    newGene = current[0][:i] + letter + current[0][i + 1:]
                    # If new gene is in bank and not in visited, add to stack and visited
                    if newGene in bank and newGene not in visited:
                        stack.append((newGene, current[1] + 1))
                        visited.add(newGene)
        # If endGene isn't reached, return -1
        return -1