# variable and names

brand = "Audi"
cars = 50
space_in_a_car = 4
drivers = 10
passengers = 70
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven


print("The brand name", brand)
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")