# assigns value 100 to the name cars
cars = 100
# assigns the value 4.0 to space_in_a_car
space_in_a_car = 4.0
# assigns 30 to drivers
drivers = 30
# assigns 90 to passengers
passengers = 90
# subtracts drivers from cars, 100 - 30
cars_not_driven = cars - drivers
# assigns cars_driven to the value of drivers
cars_driven = drivers
# assign the result of cars_driven times space_in_a_car to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# divide number of passengers by cars_driven and assign the result to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#! Study Drill 6
mask = 17
print("A 24 bit netmask has this many usable IPs", ((2 ** (32 - mask)-2)))
#!

################################################################################
################################################################################

# Study Drills
#! = my answer
#
# When I wrote this program the first time I had a mistake, and Python told me about it like this:
#
# Traceback (most recent call last ): File ”ex4.py”, line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger NameError: name ’car_pool_capacity ’ is not defined
#
# Explain this error in your own words. Make sure you use line numbers and explain why. Here are more study drills:
#
#! Incorrect Variable name.  car_pool_capacity vs carpool_capacity.  the former was not defined
#
# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
#
# 2. Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you
# need 4.0 instead of just 4 so that it is floating point.
#
# 3. Write comments above each of the variable assignments.
#
# 4. Make sure you know what = is called (equals) and that its purpose is to give data(numbers,strings, etc.) names (cars_driven, passengers).
#
#! The = is an assignment operator. It doesn't check for equivalance.
#
# 5. Remember that _ is an underscore character.
#
# 6. Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names are also i, x, and j.
