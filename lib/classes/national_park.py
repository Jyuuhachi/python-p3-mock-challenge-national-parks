class NationalPark:

    def __init__(self, name):
        self._name = name
        self._trips = []
        self._visitors = []
        self.made = True
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self.made == True:
            raise Exception("can't change park name!")
        else:
            if type(value) == type(""):
                self._name = value
            else:
                raise Exception("Name must be a string")
            
    @property
    def trips(self):
        return self._trips
    @trips.setter
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if type(new_trip) == type(Trip):
            self._trips.append(new_trip)
        else:
            raise Exception("Must be an instance of the Trip class")
        
    @property
    def visitors(self):
        return self._visitors

    @visitors.setter
    def national_parks(self, new_visitor=None):
        from classes.visitor import Visitor
        if type(new_visitor) == type(Visitor):
            self._visitors.append()
        else:
            raise Exception("Must be an instance of Visitor class")
                
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass
