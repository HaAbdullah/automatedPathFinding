from tabulate import tabulate
import replit, time

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
        self.times = 0
        self.graphs = []
        self.locations = {}


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
          self.ogFuel = self._cars[id][0]
          self.alphaFuel = max(self._cars.items())



        

    def move_car(self, id, new_x, new_y):
        global ogFuel
        """Move a car in the system.

        The car called <id> should be moved to position (<new_x>, <new_y>).

        @type self: CarManager
        @type id: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id in self._cars:
        
            if self.times == 0:
              alphaFuel = self._cars[id][0]
            self.times += 1
          
            fuel_diff = abs(new_x - self._cars[id][1]) + abs(new_y - self._cars[id][2])
            ogFuel = CarManager.get_OG_fuel(self, id)
            if ogFuel >= fuel_diff:
              self._cars[id][0] -= fuel_diff
              
              self._cars[id][1] = new_x
              self._cars[id][2] = new_y
              self.locations[id] = ((new_x, new_y))
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

    def get_OG_fuel(self, id):
      return self.ogFuel

    def get_graphs(self):
      return self.graphs

    def get_alpha_fuel(self, id):
      fuels = []
      for i in self._cars:
        fuels.append(self._cars[i][0])
      self.alphaFuel = max(fuels)
      return self.alphaFuel


class Car:
    """A car in the Super system.

    Fill in the public or private attributes for this class!
    """
    def giveGrid(self, instance):
      self.ogFuel = CarManager.get_OG_fuel(instance, id)
      self.alphaFuel = CarManager.get_alpha_fuel(instance, id)
      myData = [x[:] for x in [[" "] * self.alphaFuel] * self.alphaFuel] 
      return myData
      
      
    def displayGrid(self, instance):
      plane = Car.giveGrid(self, instance)
      X, Y = CarManager.get_car_position(instance, "Benz")
      self.alphaFuel = CarManager.get_alpha_fuel(instance, "Benz")
      #print(instance.locations[id][0])
      
      #plane[instance.locations[id][0] + (self.alphaFuel//2)][instance.locations[id][1]+ (self.alphaFuel//2)] += "X"
      for id in instance._cars.keys():
        plane[instance._cars[id][2]+ (self.alphaFuel//2)][instance._cars[id][1]+ (self.alphaFuel//2)] += id[-1] + " "
        graph = []
        
        i = len(plane) - 1
        while i >= 0:
          graph.append(plane[i])
          i -= 1

 
      graphs = CarManager.get_graphs(instance)
      graphs.append(graph)
      print(tabulate(graph, tablefmt='fancy_grid'))

      

    def playMovement(self, instance):
      graphs = CarManager.get_graphs(instance)
      replit.clear()
      for graph in graphs:
        replit.clear()
        print(tabulate(graph, tablefmt='fancy_grid'))
        time.sleep(2)
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
