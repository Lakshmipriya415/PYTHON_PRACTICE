class Fan:
    def __init__(self,make,radius,colour):
        self.make =make
        self.radius=radius
        self.colour=colour
        self.speed=0 #intally 0 speed
        self.is_on=False  #fan is of intially
    def __repr__(self):
        return repr((self.make,self.radius,self.colour,self.speed,self.is_on))

    def switch_on(self):
        self.is_on=True
        self.speed=3

    def switch_off(self):
        self.is_off=False
        self.speed=0
    
    def increase_speed(self):
        if self.is_on and self.speed<5:
            self.speed+=1

    def decrease_speed(self):
        if self.is_off and self.speed > 0:
            self.speed-=1

fan=Fan("Manufacturer 1", 5, "green")
print(fan)


fan.switch_on()
print(fan)

fan.increase_speed()
print(fan)

fan.switch_off()
print(fan)






