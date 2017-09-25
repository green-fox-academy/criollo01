''' Create Station and Car classes
- Station
  - gas_amount
  - refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
- Car
  - gas_amount
  - capacity
  - create constructor for Car where:
    - initialize gas_amount -> 0
    - initialize capacity -> 100'''

class Station(object):
    def __init__(self):
        self.gas_amount = int(100)
    
    def refill(self, car):
        self.gas_amount -= car.capacity
        return self.gas_amount

class Car(object):
    def __init__(self):
        self.gas_amount = int(0)
        self.capacity = int(100)
    

Kia = Car()
Omv = Station()

print(Omv.refill(Kia))