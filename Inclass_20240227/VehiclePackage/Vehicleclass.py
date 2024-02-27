
class Vehicle:
    '''
    Vehicle Class
    This cllass models a vehicle on a used car lot
    Change order: we need to add max speed  to the  model
    Change order: need a way to read max speed 
    Need to use constructor without max speed
    '''
    # Constuctor. Its called when... we instantiate an object of vehicle type 
    def __init__(self, type, color, max_speed = None):
        '''
        @patam type = The kind of vehicle
        @param max_speed: maximum speed of the Vehicle, defualts to None
        '''
        self.type = type;
        #self._thisisprivate = 42
        self.max_speed = max_speed; # save a copy in the 
    # a instance methof. It operates on an instance of the Vehicle class 
        self.color = color 
    def printType(self):
        print(self.type);
    def getSpeed(self):   # a getter
        return self.max_speed
    def getColor (self):
        return self.color
    
    
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass