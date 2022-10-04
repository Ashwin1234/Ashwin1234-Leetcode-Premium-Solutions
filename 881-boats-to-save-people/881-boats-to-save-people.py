class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        left = 0
        count = 0
        right = len(people) - 1
        people = sorted(people)
        while(left <= right):
            count = count + 1
            if people[left] + people[right] <= limit:
                left = left + 1
            
            right = right - 1
        return count
                