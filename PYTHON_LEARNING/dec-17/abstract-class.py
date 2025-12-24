from abc import ABC,abstractmethod
class Abstractdemo(ABC):                 #abstract class
    @abstractmethod
    def Housinginterest(self):      #abstract method
        None
    @abstractmethod
    def Vehicleinterest(self):
        None

class SBI(Abstractdemo):               #concrete classs, means no abstarct even one also
    def Housinginterest(self):         # should be same method in conncrete and abstarct otherwise throw error, TypeError: Can't instantiate abstract class SBI with abstract methods VehicleInterest
        print("8.5 interest")
    def Vehicleinterest(self):
        print("5.5 interest")

sbiobj=SBI()
sbiobj.Housinginterest()
sbiobj.Vehicleinterest()

