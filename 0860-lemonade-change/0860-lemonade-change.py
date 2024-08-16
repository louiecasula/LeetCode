class Solution:
    def lemonadeChange( self, bills: List[int]) -> bool:
        # Keep a five and ten counter
        five = ten = 0
        # Iterate bills,
        for b in bills:
            # If bill is 5, increment five
            if b == 5:
                five += 1
            # Elif bill is 10,
            elif b == 10:
                # If five > 0, increment ten and decrement five
                if five >= 1:
                    five -= 1
                    ten += 1
                # Else, return false
                else:
                    return False
            # Else,
            else:
                # If ten > 0 and five > 0, decrement both
                if ten >= 1 and five >= 1:
                    five -= 1
                    ten -= 1
                # Elif five > 2, decrement five by 3
                elif five >= 3:
                    five -= 3
                # Else, return false
                else:
                    return False
        # Return true
        return True