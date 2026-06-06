class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            total = people[right]
            right -= 1
            if left <= right and total + people[left] <= limit :
                total += people[left]
                left += 1
            boats += 1
        return boats