class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Keep an output stack and current element
        out = []
        # Iterate asteroids,
        for a in asteroids:
            # While current asteroid is negative and top of stack is positive,
            while out and a < 0 and out[-1] > 0:
                # If curr is larger than top, remove top
                if abs(a) > abs(out[-1]):
                    out.pop()
                # If curr is smaller than top, set curr to 0
                elif abs(a) < abs(out[-1]):
                    a = 0
                # If they're equal size, set curr to 0 and remove top
                else:
                    a = 0
                    out.pop()
            # If current is still here, push current asteroid to top of stack
            if a:
                out.append(a)
        # Return output
        return out