# Polymorphism is often used in Class methods
# , where we can have multiple classes with the same method name.

class Beast_wheels:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def move(self):
        print("smash")
class Ship:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def move(self):
        print("sail")
class airplanes:
    def __init__(self,name,flight):
        self.name=(name)
        self.flight=(flight)
    def move(self):
        print("fly")
# all these are objects
Beast1=Beast_wheels("tiger shark",500)#
Ship1=Ship("tycoon",459)
PLane1=airplanes("Falcon","350")
for t in Beast1,Ship1,PLane1:
    t.move()
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()