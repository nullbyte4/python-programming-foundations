"""Module 2 practice: list indexing, in-place mutation, and sorting."""

# Create a list. Valid indexes run from 0 to len(tasks) - 1, or from -1 to
# -len(tasks). Any other index raises IndexError: list index out of range.
tasks = ["Clean the Kitchen", "Study Math", "Work in my personal project", "Buy food"]
first_position = tasks[0]
last_position = tasks[-1]
length = len(tasks)

print(f"The first position of the tasks List is: {first_position}")
print(f"The last position of the tasks List is: {last_position}")
print(f"The length of the list is: {length}")


# Lists are mutable: .append() changes the same list and returns None, so
# writing tasks = tasks.append(...) would rebind tasks to None and lose the list.
tasks.append("Clean the room")
print(tasks)

# .insert(index, value) adds at that index and shifts the later items right.
tasks.insert(1, "Clean the car")
print(tasks)

# .remove(value) deletes the first matching value, not a position.
# A missing value raises ValueError.
tasks.remove("Clean the car")
print(tasks)

# .pop() removes the last item and returns it, so the result can be kept.
last_task = tasks.pop()
print(last_task)
print(tasks)

# del removes the item at a known index and does not return a value.
del tasks[0]
print(tasks)

# sorted() returns a NEW sorted list and leaves tasks unchanged.
tasks_sorted = sorted(tasks)
print(tasks_sorted)
print(tasks)

# .sort() reorders tasks in place and returns None, so do not reassign it.
tasks.sort()
print(tasks)





