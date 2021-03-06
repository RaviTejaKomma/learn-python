__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
This lesson introduces the basic assert statement in python. assert is generally used to 'assert' the truth of an
expression. It takes the form assert <expr>, <optional message>. If <expr> evaluates to False an AssertionError is raised with
the <optional message>. If is evaluates to True, nothing happens.

 In the tests below, replace the blanks with values so that the resulting expression is True.
'''


def test_assert_true():
    assert True #This should be True -- replace ___ with True.

def test_assert_true_with_message():
    assert True, "This is the failure message" # replace ___ with True to stop seeing the assertion error
    # if we repalce the ___ with False it shows an assertion error along with the message

def test_assert_equality():
    assert 7 == 2 + 5   #replace __ with the expected value

#Fill in __ in the statements below to make the asserts succeed
def test_make_assert_true_1():
    assert 9 > 7, "Fill in a value greater than 7"

#you can use the interpreter to find the value of 2**30
def test_make_assert_true_2():
    assert 2**31 > 2**30, "Fill in value greater than 2**30"

def test_make_assert_true_3():
    s1 = "Hello, World"
    s2 = s1
    assert s1 == s2

three_things_i_learnt = """
-  python is ascripting language and it is far better than other languages like c,c++,java etc
-  i have learnt about the use of assert
-  i have learnt about the mathematical operators and comparision operators
"""

