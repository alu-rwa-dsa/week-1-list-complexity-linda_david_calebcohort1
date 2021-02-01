from timeit import Timer

# First Question
# run time of an alogorithm
def run_time():
  for i in range (10):
    pass
if __name__=='__main__':
    t = Timer("run_time()", "from __main__ import run_time")
    print("This is the Runtime for this program: " , t.timeit())