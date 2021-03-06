__author__ = 'Ravi Teja'

notes = '''
In python lambda's are used to define simple anonymous single expression functions. They are commonly used to pass small
functions as parameters to higher order functions (ie) functions which take other functions as parameters or return
functions.

They are a corner feature in python. The only reason I included this lesson is so that you can read code that uses it.

http://python-history.blogspot.in/2009/04/origins-of-pythons-functional-features.html
'''
from placeholders import *

#func_invoker is a higher order function. It takes a func and its arguments and returns the result of invoking it.
def func_invoker(func, *args):
    result = func(*args)
    if result is None:
        return "func returned nothing"
    else:
        return result

def test_lambda_syntax():
    # both are equivalent
    lambda_increment = lambda x : x+1
    def nested_func(x):
        return x+1

    assert 11 == func_invoker(lambda_increment, 10)
    # this is the common usage of lambda
    assert 11 == func_invoker(lambda x : x+1, 10)
    assert 11 == func_invoker(nested_func, 10)

    #write your first lambda below !
    assert 12 == func_invoker( lambda x:x+2, 10)


def test_lambda_has_access_to_locals():
    value = 10
    assert 20 == func_invoker(lambda x: x+value, 10)

    value = 20
    assert 30 == func_invoker(lambda x: x+value, 10)

def test_lambda_locals_are_resolved_at_runtime():
    value = 10
    lambda_add = lambda x : x + value
    value = 30
    assert 40 == func_invoker(lambda_add, 10)

# this is a higher order function which returns a function
def create_adder(value):             ################ important ##################
    return lambda x : x + value

def test_lambda_local_binding():
    adder_1 = create_adder(10)
    adder_2 = create_adder(20)

    assert 110 == adder_1(100)
    assert 120 == adder_2(100)


three_things_i_learnt = """
-
-
-
"""