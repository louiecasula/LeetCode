class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Keep an output variable
        out = numBottles
        # While there are bottles,
        while numBottles >= numExchange:
            # Increment temp by numBottles // numExchange
            temp = numBottles // numExchange
            out += temp
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
            # 
        # Return output variable
        return out