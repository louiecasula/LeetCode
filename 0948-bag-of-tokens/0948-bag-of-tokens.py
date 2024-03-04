class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort tokens
        tokens = sorted(tokens)
        score = 0
        # While loop
        while True:
            print("score: ", score)
            # If the cheapest token < power, face it up
            if tokens and tokens[0] <= power:
                power -= tokens[0]
                del tokens[0]
                score += 1
                continue
            # If there are more than 1 tokens and power + expensivest > cheapest, face it down
            if len(tokens) > 1 and (power + tokens[len(tokens) - 1]) > tokens[0] and score > 0:
                power += tokens[len(tokens) - 1]
                del tokens[len(tokens) - 1]
                score -= 1
                continue
            # Return score
            return score