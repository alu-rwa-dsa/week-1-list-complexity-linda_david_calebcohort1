from memory_profiler import profile

# Second Question
# Space used by an algorithm
@profile
def my_func():
   for i in range (10):
     return i
if __name__ == '__main__':
   my_func()
