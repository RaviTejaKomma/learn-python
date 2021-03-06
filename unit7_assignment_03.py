__author__ = 'Kalyan'

profiling_cprofile = '''
This is the tool of choice for analyzing large programs (parallel to the debugger). The profiler adds its own overhead
but for relative comparison of time spent, it is very very useful.

http://pysnippet.blogspot.in/2009/12/profiling-your-python-code.html
http://docs.python.org/2/library/profile.html in particular http://docs.python.org/2/library/profile.html#instant-user-s-manual

In particular, make sure you learn how to use pstats and running cProfile from command line as described in the
first post using a sample program before doing this assignment.

python -m cProfile [-o output_file] [-s sort_order] myscript.py

For this assignment learn to use the cProfile and pstats modules from the command line.
1. run the cprofile and collect a stats file
2. learn to use the stats file separately.
3. bypass the stats creation and directly print the output to console.

compare the cumulative times of these methods and then calculate per call times.
'''
import cProfile
from unit7_conversion_methods import *


def log(func):
    def inner(*args,**kwargs):
        funcpath=func.__name__+'.profile'
        profile=cProfile.Profile()
        return1=profile.runcall(func,*args,**kwargs)
        profile.dump_stats(funcpath)
        return return1
    return inner

#invoke each of the 4 methods 5 times in a loop for count=10000. Then run this in the profiler.
@log
def profile_profiler():
    actuals=[]
    count=10000
    functions=[numbers_string1,numbers_string2,numbers_string3,num_strings4]
    for func in functions:
        for i in range(5):
            a=func(count)


# compare the times taken per call using this method to what you found in the previous methods.
# when would you use the profiler over other methods, what additional data did you get from the profiler easily
# that would have taken more work in other methods?

# what did you learn about cProfile and pstats?

summary = '''

'''

if __name__ == "__main__":
    profile_profiler()
    import pstats
    p=pstats.Stats("profile_profiler.profile")
    p.sort_stats("cumtime")
    p.print_stats()
