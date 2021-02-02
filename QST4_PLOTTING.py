# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from time import time
from matplotlib import pyplot as plot
from guppy import hpy
from question3a import FindMax
from question3b import ToLower
from question3c import SortLs

# Question 1
# Time Graph
# create list of length 100
my_lst = list(range(1, 101))


# create function called time_f
def time_f(array):
  #create an empty list
    new_lst = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        FindMax(sub_list)
        end_time = time()
        tim_diff = end_time - start_time
        #we append the diff in time in the new list
        new_lst.append(tim_diff)
    return new_lst


tms_tkn = time_f(my_lst)

# plotting the graph
plot.title("Input Size vs Time taken for FindMax")
plot.xlabel("Size")
plot.ylabel("Time")
plot.plot(my_lst, tms_tkn)
plot.show()

#Space graph

# creating session context
h = hpy()


# create function
def tk_sp(array):
  #empty lst named space_tkn
    space_tkn = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        h.setrelheap()
        FindMax(sub_list)
        raw_string = repr(h)
        raw_string = raw_string.split()
        space = raw_string[10]
        space_tkn.append(space)
    return space_tkn


space_tkn = tk_sp(my_lst)

# plot graph
plot.title("Input Size vs Space taken Find Max")
plot.xlabel("Input size")
plot.ylabel("Space taken")
plot.plot(my_lst, space_tkn)
plot.show()


# Question 3
# Time Graph
# create list of length 100
cr_int_ls = random.sample(range(1, 101), 100)

# create function


def tk_tm(array):
    tk_tmn = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        SortLs(sub_list)
        end_time = time()
        tm_df = end_time - start_time
        tk_tmn.append(tm_df)
    return tk_tmn


tms_tkn = tk_tm(cr_int_ls)

# plot graph
plot.title("Input Size vs Time take Sortls")
plot.xlabel("Input size")
plot.ylabel("Time taken")
plot.plot(cr_int_ls, tms_tkn)
plot.show()
