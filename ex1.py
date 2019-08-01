# -*- coding: utf-8 -*-
import time
import random
import datetime
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
country = "KAZAKHSTAN"

#print "There are", cars, "cars available."
#print "There are only", drivers, "drivers available."
#time.sleep(random.randrange(1,6))
#print "There will be", cars_not_driven, "empty cars today."
#print "We can transport", carpool_capacity, "people today."
#print "We have", passengers, "to carpool today."
#print "We need to put about", average_passengers_per_car, "in each car."
print "pam" + str(datetime.datetime.now())
"""dicts_from_file = []
with open('wc_list.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))
print dicts_from_file[0]
file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[0].rstrip() + "_" + ".html","w")"""
