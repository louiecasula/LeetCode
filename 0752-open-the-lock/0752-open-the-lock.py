class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Edgecase: deadends contains "0000"
        if "0000" in deadends:
            return -1
        # Keep a stack and a visited set for BFS
        stack = []
        stack.append(("0000", 0))
        visited = {"0000"}
        # While the stack isn't empty,
        while len(stack) > 0:
            # If the shifted combo is the end, return it's level
            current = stack.pop(0)
            if current[0] == target:
                return current[1]
            # Else, check all possible new combos
            for i in range(len(current[0])):
                for alt in [-1, 1]:
                    dig = str((int(current[0][i]) + alt) % 10)
                    newCombo = current[0][:i] + dig + current[0][i + 1:]
                    # If new combo isn't in visited or deadends, add to stack and visited
                    if newCombo not in visited and newCombo not in deadends:
                        stack.append((newCombo, current[1] + 1))
                        visited.add(newCombo)
        # If target isn't reached, return -1
        return -1