__author__ = 'Kalyan'

notes = '''
Generators are a easy way to create your own custom iterators. They look like
functions but do a lot of heavy lifting under the covers.

They are also useful when you want to 'generate' data on demand rather than
create all data at one shot - typically in memory constrained scenarios.

You can also think of generators as resumable functions. The caller needs to keep
calling next() to keep moving the function forward and at every stop point where you
have a yield or return the generator can return a new piece of data.
'''

from placeholders import *

# The state of the function is saved between yields and re-invoked on call to next.
def demo_generator():
    yield "how"
    yield "are"
    yield "you?"

def test_generator_type():
    assert "function" == type(demo_generator).__name__  #definition is a function
    assert "generator" == type(demo_generator()).__name__ #once you invoke it, you get a generator

def test_generator_is_an_iterator1():
    assert False == hasattr(demo_generator, "next")
    assert True== hasattr(demo_generator(), "next")

def test_generator_is_an_iterator2():
    result = demo_generator()
    try:
        assert "how" == next(result)  # builtin which calls the iterator.next()
        assert "are" == next(result)
        assert "you?" == next(result)
        assert StopIteration == next(result)
    except StopIteration as si:
        assert True

    assert "how.are.you?" == ".".join(demo_generator()) #join takes a iterable

# Note that this function takes any sequence, and returns a reversed form
# element by element, so at no point is a new reversed sequence object
# created though to the consumer it appears like a sequence.
def demo_reverse(sequence):
    for index in range(len(sequence)-1, -1, -1):
        yield sequence[index]


def test_generator_reverse():
    result = []
    # note, since the generator is an iterator too, we can use a normal for loop on it.
    for item in demo_reverse("Hello World"):
        result.append(item)
    assert ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H'] == result

def test_range_allocates_memory():
    try:
        for item in range(100 * (10**9)):
            if item%5 == 1:
                break
    except OverflowError as ofe :  # what error do you get when you allocate 100 billion ints?
           assert True

# range using a generator (xrange does something similar)
def demo_range(limit):
    value = 0
    while value < limit:
        yield value
        value = value + 1

def test_generator_range_does_not_allocate_memory():
    for item in demo_range(100 * (10**9)):
        if item%5 ==1:
            break
    assert True # did you reach here without any memory exception?


#write a statement that can collect all results from the generator into a list
def demo_generator_to_list(generator):
    result=[]
    for i in generator:
        result.append(i)
    return result

def test_collapse_generator():
    assert [0,1,2,3] == demo_generator_to_list(demo_range(4))
    assert ["how", "are", "you?"] == demo_generator_to_list(demo_generator())

def test_generator_return():
    def func():
        yield 1
        yield 2
        return ##################### None is being returned
        yield 3
    assert [1,2] == demo_generator_to_list(func())

def test_generator_control_flow():
    def func():
        for x in range(5):
            yield x
        yield 10
    assert [0,1,2,3,4,10] == demo_generator_to_list(func())

def test_generator_exception():
    def func():
        try:
            yield 10
            raise Exception("some message")
        except Exception as ex:
            yield 20
        else:
            yield 40
        finally:
            yield 50
        yield 30

    assert [10,20,50,30] == demo_generator_to_list(func())

# Note that this is an infinite generator. The client is responsible for stopping when he has had enough!
def evens():
    cur = 0
    while True:
        yield cur
        cur += 2

def test_evens():
    gen = evens()
    for num in xrange(1000):
        assert num * 2  == gen.next()

    for num in xrange(1000):
        assert 2 * 999 + (num + 1) * 2 ==gen.next()

    # why is this code a bad idea?
    # all = list(gen) ___________________________________gen generates an infinite loop we will get an memory error

# Now apply what you have learnt about generators.

# Write a python generator function which generates fizz buzz tuples infinitely.
# Every successive call to next on the generator should return (index, <content>)
# where index starts from 1 and increases by one every call.
#
# The content should be "fizz" for multiples of 3, "buzz" for multiples of 5 and "fizz", "buzz" for multiples
# of both 3 and 5.
#
# e.g. the first 5 calls to the generator should return (1, None), (2, None), (3, "fizz"), (4, None), (5, "buzz")
# for 15th call the result will be (15, "fizz", "buzz")


def fizz_buzz():
    index=1
    result=()
    while True:
          if index%15==0:
              result=(index,"fizz","buzz")
          elif index%5==0:
              result=(index,"buzz")
          elif index %3 == 0:
              result=(index,"fizz")
          else:
              result=(index, None)
          yield result
          index+=1


'''
while True:
          if index%3==0:
              yield (index,"fizz")
          elif index%5==0:
              yield (index,"buzz")
          elif index % 15 == 0:
              yield (index,"fizz","buzz")
          else:
              yield (index, None)
          index+=1

'''


def test_fizz_buzz():
    gen = fizz_buzz()
    # we are testing only the 1st 1000 calls, but your generator should not hard code an upper limit.
    for num in xrange(1, 1000):
        result = gen.next()
        if num % 15 == 0:
            assert result == (num, "fizz", "buzz")
        elif num % 3 == 0:
            assert result == (num, "fizz")
        elif num % 5 == 0:
            assert result == (num, "buzz")
        else:
            assert result == (num, None)

three_things_i_learnt = """
-
-
-
"""

