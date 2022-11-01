class FileSystem:
    
    dict1 = {}
    
    def __init__(self):
        self.dict1 = {}
    
    def createPath(self, path: string, value: int):
        if len(path.split("/")) < 1 or len(path) < 1:
            return False
        parent = path[:path.rfind('/')]
        if len(parent) > 1:
            if parent not in self.dict1:
                return False
        if path in self.dict1:
            return False
        else:
            self.dict1[path] = value
            return True
            
    def get(self, path: string):
        if path in self.dict1:
            return self.dict1[path]
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)