class Evo:
    def __init__(self):
        self.driver = None
        self.distance = 0
        self.rental_distance = 0

    def has_driver(self):
        return self.driver is not None
    
    def check_no_driver(self):
        if self.has_driver():
            raise RuntimeError("already rented out")
    
    def check_has_driver(self):
        if not self.check_no_driver():
            raise RuntimeError("The car is not rented yet!")
    
    def start_rental(self, name):
        self.check_no_driver()
        self.driver = name
        self.rental_distance = 0

    def drive(self, distance):
        if distance > 0 :
            self.distance = self.distance + distance
            self.rental_distance+=distance
        else:
            raise AttributeError("distance must be positive")
        if self.driver == None:
            raise RuntimeError("No driver assigned ")
        
    def end_rental(self):
        if self.driver == None:
            raise RuntimeError("No rental started prior")
        self.driver = None
        distance_driven = self.rental_distance
        self.rental_distance = 0
        return distance_driven
    
