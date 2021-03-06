__author__ = 'Kalyan'

problem_notes = '''
For this assignment create a decorator which can be used for count profiling.

@count_calls:
- add a count attribute to the function
- count keeps track of number of calls made to the function. If the function is recursive, give a parameter
to track only top level call and not the sub calls.

You may want to give special behavior for how this decorators behave when exceptions are raised etc. but for now
just count all calls irrespective of error status.

Assume that this decorators are used in single threaded programs only for now.

I used count for testing simplicity, you could write @time_calls decorator in a very similar spirit. Try it out as a
personal exercise and see what all design issues you hit when you chain it with above!
'''
import functools

def count_calls(skip_recursion=True):
    def log(func):

        def inner(*args,**kwargs):
            if skip_recursion==True:
               if kwargs.values()[0]==True:
                  inner.count+=1
            else:
                inner.count += 1
            return func(*args)

        inner.count = 0
        return inner


    return log

def test_calls_decorator():
    @count_calls()
    def fib(n,flag =True):
        if n <= 0:
            raise ValueError("n <= 0")
        if n == 1 or n == 2:
            return 1

        return fib(n-1,flag=False) + fib(n-2,flag=False)

    assert [1, 1, 2, 3, 5 ] == [fib(i,flag=True) for i in range(1,6)]
    assert 5 == fib.count # only top calls counted.


    # with recursion, count all calls, but this time only top level calls.
    @count_calls(skip_recursion=False)
    def fib(n):
        if n == 1 or n == 2:
            return 1

        return fib(n-1) + fib(n-2)

    assert [1, 1, 2, 3, 5 ] == [fib(i) for i in range(1,6)]
    assert 19 == fib.count # all calls counted.

