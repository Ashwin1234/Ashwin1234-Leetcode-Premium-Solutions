class HitCounter:
    
    queue = []
    
    def __init__(self):
        self.queue = []
        
    def hit(self, timestamp: int):
        self.queue.append(timestamp)
        
    def getHits(self, timestamp: int):
        while len(self.queue) > 0:
            if self.queue[0] <= timestamp - 300:
                self.queue.pop(0)
            else:
                break
        return len(self.queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)