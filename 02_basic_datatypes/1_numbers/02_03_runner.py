'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
miles_run = 10

# convert run time in seconds
actual_time = 30 * 60 + 30
second_to_hour = actual_time / 3600


actual_speed_mph = miles_run / second_to_hour
actual_speed_kph = actual_speed_mph * 1.6

# print(actual_speed_mph)
print(f"The average speed in kilometers per hour is {actual_speed_kph}")