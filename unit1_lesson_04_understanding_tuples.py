__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
Tuples are yet another sequence type along the lines of strings and lists with
its own characteristics.
'''

def test_tuple_type():
    test_tuple = (1,2)   # note the syntax
    assert "tuple"== type(test_tuple).__name__

def test_tuple_length():
    colors = ('red', 'blue', 'green')
    assert 3 == len(colors)

def test_tuple_with_no_elements():
    empty = ()
    assert True == isinstance(empty, tuple)
    assert 0 == len(empty)

def test_tuple_with_one_element(): # if tuple contains only one element then it returns the element type
    test1 = (1)
    assert "int"== type(test1).__name__

    test2 = (1,)  #note the syntax used to disambiguate
    assert "tuple"== type(test2).__name__

def test_tuple_can_be_indexed():
    colors = ('red', 'blue', 'green')
    assert 'red' == colors[0]
    assert 'blue'== colors[1]
    assert 'green' == colors[2]

def test_tuple_can_be_sliced():
    colors = ('red', 'blue', 'green')
    assert ('blue','green') == colors[1:3]
    assert ('blue',) == colors[1:2]  #remember the awkward syntax for single element tuples :),,,,,,,,,, it should contain ,


def test_tuples_are_immutable():
    colors = ('red', 'blue', 'green')
    try:
        colors[0] = 'orange'                   # tuples are immutable unlike lists
    except TypeError as te:
        print te # note the exception
        assert True

def test_tuples_can_be_nested():
    top_left = (10,20)
    bottom_right = (40,50)
    rectangle = (top_left, bottom_right)

    assert 2 == len(rectangle)
    assert (10,20) == rectangle[0]
    assert 10 == rectangle[0][0]
    assert 50 == rectangle[1][1]


def test_tuple_unpacking():
    pair = (10, 20)
    a, b = pair
    assert 10== a
    assert 20 == b

    triplet = (10, 20, 30)
    try:
        a, b = triplet
        assert False # should not come here.      #why assert came here
    except ValueError as ve:
        print ve  # observe what is printed here.
        assert True

def test_sequence_conversion():
    """
    sequences can be converted across forms using the builtin functions.
    """
    word = "testing"
    tup_1 = tuple(word)
    assert ("t","e","s","t","i","n","g")== tup_1 #same as that of string tokenizer it splits the word into single characters

    list_1 = list(word)
    assert ["t","e","s","t","i","n","g"] == list_1

    list_2 = list(tup_1)
    assert ["t","e","s","t","i","n","g"] == list_2 # converting tuple into list

    word2 = str(tup_1)                             # converting into string from a tuple
    assert "('t', 'e', 's', 't', 'i', 'n', 'g')"== word2

    word3 = "".join(tup_1)                          # opposite of string tokenizer converts tuple into string
    assert "testing"== word3
                                                    #it puts the character present in between the "" between every two characters
    word4 = "".join(list_1)
    assert "testing"== word4                        # opposite of string tokenizer converts list into string


def min_max(input):
    """
    Returns a tuple of min and max of the input list. Assume input is a non empty numeric list
    Use only builtin functions from: https://docs.python.org/2/library/functions.html
    """
    return  tuple(sorted(input)[:1]+sorted(input)[-1:])  # write a line of code to return containing min and max
    #tuple(input[:1]+input[-1:]) --------------- it works for the sorted lists
    #tuple(sorted(input)[:1]+sorted(input)[-1:]) ---------------it works for any input---slicing lists and concatinating
    #tuple(sorted(input))[:1]+tuple(sorted(input))[-1:]----------------it works same as the above----slicing tuples and concatinating them



def test_min_max():
    a, b = min_max(range(1,10))
    assert a == 1
    assert b == 9

    a, b = min_max([12])
    assert a == 12
    assert b == 12


three_things_i_learnt = """
-
-
-
"""
