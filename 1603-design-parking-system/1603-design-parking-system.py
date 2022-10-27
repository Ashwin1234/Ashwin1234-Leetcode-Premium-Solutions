class ParkingSystem:
    big = 0
    medium = 0
    small = 0
    
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big = self.big - 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium = self.medium - 1
                return True
            else:
                return False
        else:
            if self.small > 0:
                self.small = self.small - 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)