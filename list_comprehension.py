# List comprehension - numbers
numbers = [1, 2, 3, 4, 5, 6]
expand_numbers = [n + 1 for n in numbers]
print(expand_numbers)

# List comprehension - strings
employees = ["Angela", "Micah", "Beth", "Alex", "Samuel", "Carol", "Mark", "Meridith"]
short_names = [name for name in employees if len(name) < 5]
print(short_names)
medium_names = [name for name in employees if len(name) == 5]
print(medium_names)
long_names_capitol = [name.upper() for name in employees if len(name) > 5]
print(long_names_capitol)

"""
Convert the list into integers and then generate a list of even numbers
"""

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings ]
result = [n for n in numbers if n % 2 == 0]
print(result)
