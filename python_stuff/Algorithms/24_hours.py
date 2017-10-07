"""
Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem.
Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on the clock when the alarm goes off.
"""

# On the fly, didn't test for false positives :)


def return_validated_time():
    time_now = int(input("What is the time now?"))
    if time_now < 0:
        return False
    elif time_now <= 23 >= 0:
        return time_now
    else:
        return False


def return_validated_alarm_time():
    alarm_time = int(input("Alarm in how many hours?"))
    if alarm_time <= 0:
        print("Alarm time must be greater than 0")
        return_validated_alarm_time()
    else:
        return alarm_time


def calculate_alarm(time_now, alarm_time):
    days_counter = 0
    while time_now + alarm_time > 24:
        days_counter += 1
        alarm_time -= 24
    if time_now + alarm_time <= 23:
        if days_counter != 0:
            print("alarm will trigger in {} days, at {}".format(days_counter, (time_now + alarm_time)))
        print("alarm will trigger today at {}".format(time_now+alarm_time))
    elif time_now + alarm_time == 24:
        print("alarm will trigger at midnight")

calculate_alarm(return_validated_time(), return_validated_alarm_time())


# current_time_string = input("What is the current time (in hours)? ")
# waiting_time_string = input("How many hours do you have to wait? ")
#
# current_time_int = int(current_time_string)
# waiting_time_int = int(waiting_time_string)
#
# hours = current_time_int + waiting_time_int
#
# timeofday = hours % 24
#
# print(timeofday)