class CarManager:
    """A class responsible for keeping track of all cars in the system.
    """

    # === Private Attributes ===
    # @type _cars: dict[str, Car]
    # A map of unique string identifiers to the corresponding cars.

    def __init__(self):
        """Create a new CarManager.

        Initially there are no cars in the system.

        @type self: CarManager
        @rtype: None
        """
        self._cars = {}

    def add_car(self, id, fuel):
        """Add a new car to the system.

        The new car is identified by the string <id>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        @type self: CarManager
        @type id: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id not in self._cars:
          self._cars[id] = [fuel, 0, 0]

    def move_car(self, id, new_x, new_y):
        """Move a car in the system.

        The car called <id> should be moved to position (<new_x>, <new_y>).

        @type self: CarManager
        @type id: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id in self._cars:
            ogFuel = self._cars[id][0]
            fuel_diff = (abs((new_x - self._cars[id][1]) + (new_y - self._cars[id][2])))
            if ogFuel >= fuel_diff:
              self._cars[id][0] -= fuel_diff
              self._cars[id][1] = new_x
              self._cars[id][2] = new_y
        pass

    def get_car_position(self, id):
        """Return the position of car <id> in the system.

        Return a tuple of the (x, y) position of the car.

        @type self: CarManager
        @type id: str
        @rtype: (int, int)
        """
        if id in self._cars:
          location = [self._cars[id][1], self._cars[id][2]]
          return tuple(location)
            

    def get_car_fuel(self, id):
        """Return the amount of fuel of car <id> in the system.

        @type self: CarManager
        @type id: str
        @rtype: int
        """
        if id in self._cars:
            return self._cars[id][0]


class Car:
    """A car in the Super system.

    Fill in the public or private attributes for this class!
    """
    # TODO: design and implement this class.
    pass
'''
manager = CarManager()

def testCases():
  manager.add_car("HONDA", 5)
  manager.add_car("FERRARI", 10)
  manager.move_car("FERRARI", 30, 40)
  print(manager.get_car_position("FERRARI"))
  manager.move_car("FERRARI", 50, 50)
  print(manager.get_car_position("FERRARI"))
  print(manager.get_car_fuel("FERRARI"))
  #print(manager._cars)
  pass

testCases()
'''
