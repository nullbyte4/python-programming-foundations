"""Module 1 practice: running a script, assigning, and reassigning variables."""

# Assign a string value to a variable label and display it.
study_topic = "History"
print(study_topic)

# Reassign the same variable label to a new string value.
study_topic = "Math"
print(study_topic)

# Independent variation: assign and reassign an integer value.
total_value = 10
print(total_value)

total_value = 5
print(total_value)


color = " bLuE "
color = color.strip().title()
print(color)


time_1 = 45
time_2 = 30
total_time_minutes = time_1 + time_2
print(total_time_minutes)

total_time_hours = total_time_minutes / 60
print(f"Total time in minutes: {total_time_minutes}")
print(f"Total time in hours: {total_time_hours}")
print(f"The Study Topic is: {study_topic}")

average_minutes = (time_1 + time_2) / 2
print(f"The average between the two times is: {average_minutes} minutes")