class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1, key = lambda x:x[1])
        slots2 = sorted(slots2, key = lambda x:x[1])
        first = 0
        second = 0
        while(first < len(slots1) and second < len(slots2)):
            if slots1[first][0] > slots2[second][1]:
                second = second + 1
            elif slots2[second][0] > slots1[first][1]:
                first = first + 1
            else:
                if min(slots1[first][1], slots2[second][1]) - max(slots1[first][0], slots2[second][0]) >= duration:
                    return [max(slots1[first][0], slots2[second][0]), max(slots1[first][0], slots2[second][0]) + duration]
                else:
                    if slots1[first][1] <= slots2[second][1]:
                        first = first + 1
                    else:
                        second = second + 1
        return []