__author__ = 'Ravi Teja'

from placeholders import *

notes = """
This lesson explores some advanced features of functions. This will help you make sense
of a lot of standard library functions when you use them.
"""

def demo(first, second=2, third=3):
    return [first, second, third]

# keyword arguments allows you to write one api without having a large number
# of overloads for various scenarios.
# NOTE: add extra arguments where necessary. First note what error you get and then fix the function invocations.
def test_function_call_with_keyword_arguments():
    assert [10,2,3] == demo(10)
    assert [10,20,3] == demo(10, 20)
    assert [10,20,30] == demo(10, 20, 30)
    assert [10,20,3] == demo(10,second=20)
    assert [10,20,30] == demo(10,second=20, third=30)
    assert [10,2,30] == demo(first=10, third=30)
    assert [10,2,30] == demo(10, third=30)
    '''
    assert [__] == demo(second=20)
    assert [__] == demo(second=20, third=30)
    these two statements will raise an error----demo() takes at least 1 argument (1 given)
    so we have to change the above function invocations as below
    assert [__] == demo(10,second=20)
    assert [__] == demo(10,second=20, third=30)
    '''

def demo_variable_args(first, *args):
    return args


def my_merge(separator, *args):
    return separator.join(args)


def test_function_with_variable_args():
    result = demo_variable_args("hello", "world")
    assert "tuple" == type(result).__name__ #this is the type of args
    assert ("world",) == result              #this is the value of args

    assert (1,2,3) == demo_variable_args("hello", 1, 2, 3)

    assert  "one.two.three"== my_merge(".", "one", "two", "three")
    assert "one,two,three" == my_merge(",", "one", "two", "three")


def demo_with_keyword_args(name, *args, **kwargs):  ##############DOUBT
    return kwargs


def test_function_with_keyword_args():
    result = demo_with_keyword_args("jack", age=10, height=100)
    assert "dict" == type(result).__name__
    assert {'age': 10, 'height': 100} == result
    assert {'age': 10, 'height': 100} == demo_with_keyword_args("jack", "address", age=10, height=100)
    assert {'age': 10, 'height': 100, 'address': 'address'} == demo_with_keyword_args("jack", address="address", age=10, height=100)


def demo_var_kw(*args, **kwargs):
    return args, kwargs


def demo_unpacking(name, *args, **kwargs):
    return demo_var_kw(*args, **kwargs)


def demo_no_unpacking(name, *args, **kwargs):
    return demo_var_kw(args, kwargs)


# Unpacking sequences into arguments is useful when you are calling other
# functions which take variable/kw args. Also read
# http://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
# Visualizer link provided at bottom.

def test_function_unpacking():
    result = demo_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert ((1,2),{"k1":"v1","k2":"v2"}) == result

    result = demo_no_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert (((1, 2), {'k2': 'v2', 'k1': 'v1'}), {}) == result   ################## take a note of this

    result = demo_var_kw(1,2, k1="v1")
    assert (((1,2),{"k1":"v1"})) == result

    result = demo_var_kw((1,2), {"k1" :"v1"})
    assert (((1, 2), {'k1': 'v1'}), {}) == result

    result = demo_var_kw(*(1,2), **{"k1": "v1"})
    assert ((1, 2), {'k1': 'v1'}) == result

    #you can unpack lists as well
    result = demo_var_kw(*[1,2], **{"k1":"v1"})
    assert ((1, 2), {'k1': 'v1'}) == result

notes_2 = """
Walk through the visualizer, first read the code a couple of times and then step through :)
http://pythontutor.com/visualize.html#code=def+demo_var_kw(*args,+**kwargs)%3A%0A++++return+args,+kwargs%0A%0Adef+demo_unpacking(name,+*args,+**kwargs)%3A%0A++++return+demo_var_kw(*args,+**kwargs)%0A%0Adef+demo_no_unpacking(name,+*args,+**kwargs)%3A%0A++++return+demo_var_kw(args,+kwargs)%0A%0Adef+test_function_unpacking()%3A%0A++++demo_unpacking(%22jack%22,+1,+2,+k1%3D%22v1%22,+k2%3D%22v2%22)%0A++++demo_no_unpacking(%22jack%22,+1,+2,+k1%3D%22v1%22,+k2%3D%22v2%22)%0A++++demo_var_kw(1,2,+k1%3D%22v1%22)%0A++++demo_var_kw((1,2),+%7B%22k1%22+%3A%22v1%22%7D)%0A++++demo_var_kw(*(1,2),+**%7B%22k1%22%3A+%22v1%22%7D)%0A%0A++++%23you+can+unpack+lists+as+well%0A++++demo_var_kw(*%5B1,2%5D,+**%7B%22k1%22%3A%22v1%22%7D)%0A%0A++++%0Atest_function_unpacking()&mode=display&cumulative=false&heapPrimitives=true&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&curInstr=0
"""


# This function shows how variable arguments can be useful to define certain kinds of functions
def simple_format(format, *args):
    """
    Returns a formatted string by replacing all instances of %X with Xth argument in args (0...len(args))
    e.g. "%0 says hello", "ted" should return "ted says hello"
    "%1 says hello to %0", ("ted", "jack") should return jack says hello to ted etc.
    If %X is used and X > len(args) it is returned as is.
    """
    index = 0
    while index < len(args):
        format = format.replace("%" + str(index), args[index])
        index += 1
    return format


def test_simple_format():
    assert "hello hari"  == simple_format("hello %0", "hari")
    assert "hari says hari"  == simple_format("%0 says %0", "hari")
    assert "hari calls ashok"  == simple_format("%1 calls %0", "ashok", "hari")
    assert "hari calls ashok and %2"  == simple_format("%1 calls %0 and %2", "ashok", "hari")

three_things_i_learnt = """
-
-
-
"""

