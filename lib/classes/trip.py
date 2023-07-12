from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:
    
    all_trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all_trips.append(self)

    @property
    def visitor(self):
        return self.visitor
    
    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor
        if type(value) == Visitor:
            self.visitor = value
        else:
            raise TypeError("visitor must be an instance of the Visitor class")
        
    @property
    def national_park(self):
        return self.visitor
    
    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark
        if type(value) == type(NationalPark):
            self.national_park = value
        else:
            raise TypeError("visitor must be an instance of the Visitor class")