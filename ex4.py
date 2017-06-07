cars = 100 #defines number of cars
space_in_a_car = 4 #defines passenger capacity per car
drivers = 30 #defines number of drivers
passengers = 90 #defines number of passengers
cars_not_driven = cars - drivers #there cannot be more cars than drivers, so subtract the number of drivers available from the total number of cars.
cars_driven = drivers #assuming there is one driver per car, this is the max number of vehicles that can be on the road.
carpool_capacity = cars_driven * space_in_a_car #If each vehicle has 4 spaces, the total number of space available is equl to the number of cars multiplied by 4 (4 + 1 driver).
average_passengers_per_car = passengers / cars_driven #distributes number of passengers evenly among the 30 drivable vehicles.

print "There are", cars, "cars available." 
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# The reason there was an error on line 8 in the
# original code is because the variable defined on
# line 5 is carpool_capacity not car_pool_capacity
