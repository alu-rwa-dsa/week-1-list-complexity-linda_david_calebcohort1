import numpy as np

# (a) of the Third Question
# Max of a list
def max_value():
  Alphabets = [23, 1, 2, 90, 10]
  max = np.max(Alphabets)
  print("The maximum number is: " , max)

print(max_value())

# (b) of the Third Question
# Make each letter a lower case
def lower_character():
  a = "MUGISHA"
  print(a.lower())

print(lower_character())

# (c) of the Third Question
# Sort number
def sort_num():
  numbers = [23, 1, 2, 90, 10]
  print(sorted(numbers))

print(sort_num())