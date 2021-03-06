__author__ = 'Ravi Teja'

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.

builtin functions: http://docs.python.org/2/library/functions.html
use constants from string module (string.XXXX) as required.

Notes:
1. Last assignment was about declarative thinking in terms of available utility functions.
   This assignment is about thinking in terms of python builtin  data types - numbers, strings, sets,
   dicts and tuples.

2. Start thinking in terms of converting one datatype to another based on what you need. Think
   in terms of set and list operations where required instead of thinking in terms of for loops and while loops.
   You need both kinds of thinking to write good code.

3. All the methods will require 1-3 lines of straight line code.

4. These methods are are meant to help you think in certain ways, some of them can be done more efficiently without
   using the data types but that is not the goal of this assignment.

Use the console to experiment and figure out the solution.

Reading material
 http://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
 https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
 https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
 It is a good idea to review the lessons as well!
'''

from placeholders import *

#This allows you to use string constants using the string.XXX notation.
import string

def get_lower_to_upper_dict():
    """
    returns a dict which contains a mapping from lower case letters to upper case letters
    Hint: see the constants in the string module, and the zip builtin function
    """
    return dict(zip(list(string.ascii_lowercase),list(string.ascii_uppercase)))
    """ in here string.ascii_lowercase,string.ascii_uppercase are two string constants
    which returns all the 26 alphabets in lowercase and uppercase respectively in the form of a string"""
    # zip function pairs up the corresponding elements in two lists and returns another list

def test_lower_to_upper_dict():
    lower_to_upper = get_lower_to_upper_dict()
    assert 26 == len(lower_to_upper)
    for x in lower_to_upper:
        y = lower_to_upper[x]
        assert 1 == len(x)
        assert x.islower()
        assert 1 == len(y)
        assert y.isupper()
        assert x.upper() == y


def get_encoding_dict():
    """
    returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
    No control flow allowed.
    """
    return  dict(zip(list(string.ascii_lowercase),range(1,27))+zip(list(string.ascii_uppercase),range(1,27)))

def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]


# This is a module variable that you can use in your code.
VOWEL_SET = set("aeiou")
def get_consonents(input):
    """
    returns the set of consonents in the input string, case is not important.
    e.g Apple and apple both return set(['p', 'l'])

    No control flow plz.
    """
    return set(input.lower())-VOWEL_SET

def test_get_consonents():
    assert set("ylf") == get_consonents("fly")
    assert set("pl") == get_consonents("APPLE")
    assert set("lp") == get_consonents("apple")
    assert set() == get_consonents("aei")


def capitalize_names(input):
    """
    Given a list of first names, capitalize them properly
    e.g ["JAMES", "jack", "HArry"] should return ["James", "Jack", "Harry"]
    Hint: use a built in function and one of the string module functions to make this happen
    """
    return map(str.capitalize,input)

def test_capitalize_names():
    assert ["James"] == capitalize_names(["JAMES"])
    assert ["Harry", "Jack"] == capitalize_names(["HArry", "jack"])
    assert [] == capitalize_names([])


def bit_count_even(number):
    """
    Returns True if the binary representation of number (>=0) has even number of 1s.
    E.g 5 (101) returns True, 6 (110) returns True,  7 (111) returns False.
    Hint: see the supported methods of string.
    """
    return  0==(bin(number)[2:].count("1"))%2

def test_bit_count_even():
    assert True == bit_count_even(0xFF)
    assert False == bit_count_even(0xFE)
    assert True == bit_count_even(0)
    assert False == bit_count_even(8)
