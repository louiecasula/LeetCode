class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Keep an output variable and a rectangle array
        out = 0
        rect = [0] * (len(matrix[0]) + 1)
        # For every row,
        for row in matrix:
            # For every element,
            for i in range(len(row)):
                # If element is 0, set rect[i] to 0,
                if row[i] == "0":
                    rect[i] = 0
                # Else, increment rect[i]
                else:
                    rect[i] += 1
            # Use a stack to update area
            stack = []
            for i in range(len(rect)):
                while stack and rect[i] < rect[stack[-1]]:
                    h = rect[stack.pop()]
                    w = 0
                    if not stack:
                        w = i
                    else:
                        w = i - stack[-1] - 1
                    out = max(out, h * w)
                stack.append(i)
        # Return max
        return out