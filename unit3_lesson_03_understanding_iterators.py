__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
Iterators are objects that represent a stream of data. next() method on an iterator returns
the next available element. StopIteration is raised when elements are finished.

Python builtins like sequences (strings, lists, tuples), sets and dicts are iterable (ie) you can call iter(obj) on them
and get an iterator object on their data.

Iterators allows us to write functions and implement language features which can
work with any iterable instead of having specialized implementation for each of
list, tuple, string etc.
'''

def test_iterator_type():
    list_iter = iter(["one", "two", "three"])
    assert 'listiterator' == type(list_iter).__name__
    assert True == hasattr(list_iter, "next")############## DOUBT ##############

    string_iter = iter("hello")
    assert "iterator" == type(string_iter).__name__
    assert True == hasattr(string_iter, "next")

    tuple_iter = iter((1,2,3))
    assert "tupleiterator" == type(tuple_iter).__name__
    assert True == hasattr(tuple_iter, "next")

def test_int_iterable():
    try:
        iter(10)             ########### int object is not iterable
    except TypeError as te:  # replace by appropriate except so this test passes
        pass

def test_enumerate_iter():
    list_iter = iter(["one", "two", "three"])  ############ take a note of this
    try:
        assert "one" == list_iter.next()
        assert "two" == list_iter.next()
        assert "three" == list_iter.next()
        assert None == list_iter.next() #note what happens when items are finished.
    except StopIteration as se :
        pass

#note this function which can convert any iterable into a list.
def convert_to_list(iterable):
    seq_iterator = iter(iterable)      ########## important ###########
    result = []
    try:
        while True:
            item = seq_iterator.next()
            result.append(item)
    except StopIteration as se:
        return result

def test_convert():
    assert ['h','e','l','l','o'] == convert_to_list("hello")
    assert [1,2,3,4] == convert_to_list((1,2,3,4))
    assert [0,1,2,3,4]== convert_to_list(range(5))


def test_join():
    #string.join also works using the iteration protocol!
    #accepts any iterable
    assert "h.e.l.l.o" == ".".join("hello")
    assert "hello.world" == ".".join(["hello", "world"])
    assert "hello.there" == ".".join(("hello", "there"))

    try:
        ".".join([1,2,4]) #does not accept all element types though!
    except TypeError as te :
        assert True

def test_multiple_iterators():
    # each iterator has state independent of other iterators.
    fruits = ["apple", "orange", "banana"]
    iter1 = iter(fruits)
    iter2 = iter(fruits)

    assert "apple" == iter1.next()
    assert "apple" == iter2.next()

    assert  ["orange", "banana"]== list(iter1)
    assert ["orange", "banana"] == list(iter2)


def test_iter_on_iterator():
    fruits = ["apple", "orange", "banana"]
    iter1 = iter(fruits)
    iter2 = iter(iter1)

    assert True == (iter1 is iter2)
    # iter on iterator object returns the same object by convention. This facilitates functions to work on either iterables
    # or iterators using the same protocol of calling iter on them.
    # this implies that convert to list can take any iterable or an iterator in practice
    assert ["apple", "orange", "banana"] == convert_to_list(iter1)


def test_for():
    # for loop works by calling iter on the target object.
    l = [1,2,3]
    # this is magic method that needs to be implemented by any object that supports iteration. iter(l) just calls l.__iter__()
    iter1 = l.__iter__()

    result = []
    for x in l:
        result.append(x)
    assert [1,2,3] == result

    result = []
    for x in iter1:
        result.append(x)
    assert [1,2,3] == result

    result = []
    for x in iter1:
        result.append(x)
    assert [] == result  #what happened here?

    result = []
    for x in l:
        result.append(x)
    assert [1,2,3]== result

# list creation also uses the iterator protocol!
# note via help(list) in console. we have already used this, you know how it works now!
def test_list_creation():
    assert ['h','e','l','l','o'] == list("hello")
    assert [1,2,3,4]== list((1,2,3,4))
    assert [0,1,2,3,4]== list(range(5))

# tuple constructor function works the same way!
def test_tuple_creation():
    assert ('h','e','l','l','o') == tuple("hello")
    assert (1,2,3,5)== tuple([1,2,3,5])

# Note that none of these functions below know which exact type they are working
# with, as long as their parameters support the iterator protocol they will work.
# Consider the immense productivity gain you have with this approach.
def test_functions_that_work_on_iterables():
    test_dict = {"one": 1, "two":2}
    assert ["one","two"] == sorted(test_dict)
    assert ['two', 'one'] == list(test_dict) ################ DOUBT ################3

# Go through the functions at http://docs.python.org/2/library/functions.html
# and enter all the functions that operate on iterables into the funcs list.
def test_find_builtins_that_work_on_iterables():
    funcs = ["all","any"]           ################## all(),any() are functions
    assert 2 == len(funcs)          ######################### DOUBT



# Now apply what you have learnt.
# This function implements a map. It goes through the iterable and applies func on each of the elements and
# returns a list of results.
# Don't use a for loop or the builtin map function :). Use exceptions, while loop and iter.
def my_map(func, iterable):
    iter1=iter(iterable)
    result=[]
    try:
        while iter1:
              result.append(func(iter1.next()))      # if i don't use .next() function here the loop will not break
    except StopIteration as se:
           return result

def double(x):
    return 2 * x

import string

def test_my_map():
    assert range(0, 20, 2) == my_map(double, range(10))
    assert list(string.ascii_uppercase) == my_map(string.upper, string.ascii_lowercase)

    list_iter = iter(range(10))
    assert range(0,20,2) == my_map(double, list_iter)
    assert [] == my_map(double, list_iter) #if you did not understand this, go through the lesson again.


three_things_i_learnt = """
-
-
-
"""