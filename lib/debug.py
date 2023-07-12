#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    test_visitor = Visitor("matt hardy")
    test_national_park = NationalPark("battery park")
    test_trip = Trip(test_visitor, test_national_park, "25th", "30th")
    ipdb.set_trace()
