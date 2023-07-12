class Visitor:

    def __init__(self, name):
        self._name = name
        self._national_parks = []

    def __str__(self):
        return f"Visitor object with name {self._name}"
        
    def trips(self):
        from classes.trip import Trip
        visitor_trips = []
        for trip in Trip.all_trips:
            if trip.visitor == self:
                visitor_trips.append(trip)
        return visitor_trips
    
    def national_parks(self):
        from classes.trip import Trip
        visitor_parks = []
        for trip in Trip.all_trips:
            for i in visitor_parks:
                if trip.national_park.name == visitor_parks[i].name:
                    continue
                else:
                    visitor_parks.append(trip)
        return visitor_parks


        
    @property
    def national_parks(self):
        return self._national_parks

    @national_parks.setter
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if type(new_national_park) == type(NationalPark) and type(new_national_park) != None:
            self._national_parks.append()
        else:
            raise Exception("Must be an instance of NationalPark class")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == type(""):
            if len(value) >= 0 and len(value) <= 14:
                self._name = value
            else:
                raise ValueError("Name can only be 1 - 15 characters long")
        else:
            raise TypeError("Name can only be a string")