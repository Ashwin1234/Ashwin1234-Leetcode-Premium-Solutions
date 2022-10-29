class Logger(object):
    
    dict1 = {}
    
    def __init__ (self):
        self.dict1 = {}
        
    def shouldPrintMessage(self, timestamp: int, message: string):
        if message in self.dict1:
            if timestamp - self.dict1[message] >= 10:
                self.dict1[message] = timestamp
                return True
            else:
                return False
        else:
            self.dict1[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)