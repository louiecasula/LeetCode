class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Keep a counter variable
        boats = 0
        # Sort people and make it a queue
        people.sort()
        people = deque(people)
        # Add the largest and smallest to reach limit, increment counter when limit reached
        while people:
            sublim = people.pop()
            if people and people[0] + sublim <= limit:
                sublim += people.popleft()
            boats += 1
        # Return counter
        return boats