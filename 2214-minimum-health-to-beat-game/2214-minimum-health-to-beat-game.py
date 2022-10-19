class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        count = 0
        max_damage = -1
        for ele in damage:
            if ele > max_damage:
                max_damage = ele
        
        count = sum(damage)
        count = count - max_damage
        if max_damage > armor:
            count = count + max_damage - armor + 1
        else:
            count = count + 1
        
        return count
            
            