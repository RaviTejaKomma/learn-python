__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
Functions are the basic unit of modularization in python. You use functions to group
together a meaningful action and use it when you need it.

The feature set of functions in python is richer than every major programming
language and makes it easy to expose elegant and usable apis.

This is a big topic, we will revisit this topic again.
'''

# here's a simple function. returns nothing
def my_print(x):
    print x

# this is another function. Note the syntax. Returns a value
def my_increment(x):
    return x + 1

# another function, it is common to return multiple values as a tuple.
def my_min_max(numbers):
    return min(numbers), max(numbers)

# functions are kinds of objects, they have a type too!
def test_function_type():
    assert 'function' == type(my_print).__name__
    assert 'function'== type(my_increment).__name__
    assert 'function' == type(test_function_type).__name__

# functions are objects which can be 'called'
def test_function_callable_type():
    assert False == callable(1)
    assert True == callable(my_increment)
    assert False == callable(my_increment(10))   ################take a note of this

# functions can be held by references just like any other object
def test_function_assignment():                  ################### take a note of this
    demo = my_increment
    result = demo(20)
    assert 21 == result

# every function returns an object, even when it does not!
def test_every_function_returns_something():
    result = my_print(10)
    assert None == result                         ##################### take a note of this

    result = my_increment(10)
    assert 11 == result

    result = my_min_max([20, 30, 5])
    assert (5,30)== result


def demo1():
    """returns 10"""
    return 10


def demo2():
    return 20

#The documentation of every function, if the author wrote it, is available at runtime.
#This makes it easy to access help from console or build specialized help commands like help.
def test_function_documentation():
    assert "returns 10" == demo1.__doc__
    assert None == demo2.__doc__


def my_callfunc(func):
    return func()

# functions can be passed around.
def test_functions_can_be_passed_as_objects():
    assert 10 == my_callfunc(demo1)
    assert 20 == my_callfunc(demo2)


# an example of a default argument
def my_greet(greeting, name="world"):
    return "{0} {1}".format(greeting, name)


def test_default_arguments():
    assert  "Hello world"== my_greet("Hello")
    assert "Hello john" == my_greet("Hello", "john")


def my_add_to_list1(sequence, target=[]):
    """                                                    #########################3 take a note of this
    Uses a mutable default, usually leads to unexpected behavior
    """
    target.extend(sequence)
    return target


def my_add_to_list2(sequence, target=None):
    """
    Uses None as default and creates a target list on demand.
    """
    if target is None:
        target = []
    target.extend(sequence)
    return target


def test_function_defaults_are_evaluated_at_definition_time():
    assert ['h','i'] == my_add_to_list1("hi")
    assert ['h','i','b','y','e'] == my_add_to_list1("bye")

    assert ['h','i'] == my_add_to_list2("hi")
    assert ['b','y','e'] == my_add_to_list2("bye")


reading_note = """
Walk through the visualizer to get a good idea of how functions are defined
and how arguments are passed. Copy paste whole link into browser.
Do this before proceeding further.

http://pythontutor.com/visualize.html#code=def+demo_parameter_passing1(x)%3A%0A++++print+%22before+addition%22,+id(x)%0A++++x+%3D+x+%2B+1%0A++++print+%22after+addition%22,+id(x)%0A%0Adef+demo_parameter_passing2(names)%3A%0A++++print+%22before+assignment%22,+id(names)%0A++++names+%3D+%5B%5D%0A++++print+%22after+assignment%22,+id(names)%0A%0Adef+demo_parameter_passing3(names)%3A%0A++++print+%22before+append%22,+id(names)%0A++++names.append(%22something%22)%0A++++print+%22after+append%22,+id(names)%0A%0Adef+test_function_params_passed_by_object_reference()%3A%0A++++x+%3D+10%0A++++print+id(x)%0A++++demo_parameter_passing1(x)%0A%0A++++names+%3D+%5B%22one%22,+%22two%22%5D%0A++++print+%22before+calling+demo_parameter_passing2%22,+id(names)%0A++++demo_parameter_passing2(names)%0A++++%0A++++print+%22before+calling+demo_parameter_passing2%22,+id(names)%0A++++demo_parameter_passing3(names)%0A++++%0Atest_function_params_passed_by_object_reference()&mode=display&cumulative=false&heapPrimitives=true&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&curInstr=0
"""

def demo_parameter_passing1(x):
    x = x + 1

def demo_parameter_passing2(names):
    names = []


def demo_parameter_passing3(names):
    names.append("something")


def test_function_params_passed_by_object_reference():
    x = 10
    demo_parameter_passing1(x)
    assert 10 == x

    names = ["one", "two"]
    demo_parameter_passing2(names)
    assert ["one","two"] == names

    demo_parameter_passing3(names)
    assert ["one","two","something"] == names


notes_2 = """
Read this finally :): http://effbot.org/zone/call-by-object.htm
"""

# Most of the python api uses the ability to pass functions as parameters,
# the tests below make you exercise them.

def find_len(input):    ############## when the input is string it returns a list with 1's where a vowel is present and 0's where a vowel is not present
    y = []              ############# when the input is a list it returns a list with number of vowels present in the correspondind input list elements
                        # it will eliminate the duplicates
    for x in range(0, len(input)):
        y.append(len(set(input[x]) & set("aeiou")))
    return y

def get_word_with_least_vowels(input): #######################DOUBTTTTTTTTTTTTTTTTTTTTTTTTTT CLARIFIED
    """
    returns the word with least number of vowels.
    """
    return min(input,key=find_len)
    # replace this with right code. Use min builtin and define a new function to pass as key.
    '''input = list(input)
    y = find_len(input)
    return input[y.index(min(y))]'''
    '''>>>min([1,0,0,1],[1],[0,0],[1,1,1])
      [0, 0]                                                 it is returning based on sum of the elements
       >>> max([1,0,0,1],[1],[0,0],[1,1,1])
       [1, 1, 1]
    '''

def test_get_word_with_least_vowels():
    assert "fly" == get_word_with_least_vowels(["apple", "joy", "fly"])
    assert "flow" == get_word_with_least_vowels(["apple", "hello", "flow"])
    # same code works for any iterable!
    assert "fly" == get_word_with_least_vowels({"apple", "joy", "fly"})
    assert "flow" == get_word_with_least_vowels(("apple", "hello", "flow"))

def get_min_max_words(input):
    """
    returns the words with the least and maximum length.
    Use min and max and pass another function as argument
    """
    return (min(input,key=len),max(input,key=len))# replace this calls to min and max
    #(sorted(input,key=len)[0],sorted(input,key=len)[len(input)-1])---------------we can use this too
def test_get_min_max_words():
    assert ("fly", "engine") == get_min_max_words(["fork", "engine", "fly"])
    assert ("fork", "fork") == get_min_max_words(["fork"])
    assert ("fork", "automobile") == get_min_max_words({"fork", "automobile", "tester"})


three_things_i_learnt = """
-
-
-
"""