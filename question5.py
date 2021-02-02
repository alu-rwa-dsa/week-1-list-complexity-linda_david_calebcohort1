# fifth Question

# Importing timeit module
from timeit import Timer

def time_taken():
  """This method is for displaying numbers upto 1000000"""
  for a in range(1000000):
    return a
if __name__=='__main__':
    t = Timer("time_taken()", "from __main__ import time_taken")
    print("This is the Runtime for this program: " , t.timeit())