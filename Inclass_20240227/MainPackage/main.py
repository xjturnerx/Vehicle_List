
from VehiclePackage.Vehicleclass import *
if __name__ == "__main__":
    #Instantiate an object if type Vehicle 
    myCorvette = Vehicle("Car","red") # Trigger a call to the instructor 
    myCorvette.printType()
    maximum_speed = myCorvette.getSpeed()
    print ("Maximum speed", maximum_speed)
    obj = myCorvette.getColor()
    print ("car color", myCorvette.getColor())
    
    #I want a list of 3 vehicles 
    
    
    myHonda = Vehicle("Car","Maroon", 100)
    myBoat = Vehicle("Boat", "White", 65)
    myUFO = Vehicle("SpaceShip","Silver",100000000)
    
    vehicleList =[myBoat,myHonda,myUFO]
    for Vehicle in vehicleList:
        Vehicle.printType()
        print(Vehicle.getSpeed)
        print(Vehicle.getColor())
        
        
    