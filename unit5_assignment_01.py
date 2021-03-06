__author__ = 'Kalyan'

notes = '''
Though it might appear as if the given tests should be able to catch all logical bugs in de_dup_and_sort, that is not the
case as the code below shows.

So be clear that some blackbox tests alone are no substitute for reasoning/taking care of the correctness yourself.

Now add a test that fails with the given code. You can assume that inputs are of right type.
'''
def de_dup_and_sort(input):
    """
    Given an input list of strings, return a list in which the duplicates are removed and the items are sorted.
    """
    input.sort()
    input=set(input)
    input = list(input)
    input.sort()  ###################################### added line ######################
    return input


# add an test input that fails with above code and then fix the above code.
def test_de_dup_and_sort_student():
    assert ["apple","banana","orange"]==de_dup_and_sort(["apple","banana","orange"])
    assert ['a','e','l','p']==de_dup_and_sort(['a','p','p','l','e'])


def test_de_dup_and_sort():
    assert ["a", "b"] == de_dup_and_sort(["b", "a", "b", "a"])
    assert ["a"] == de_dup_and_sort(["a", "a", "a"])
    assert [] == de_dup_and_sort([])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"])
    assert ["a", "b"] == de_dup_and_sort(["a", "b"]*10)
    assert ['ravi"teja"']==de_dup_and_sort([r'ravi"teja"','ravi"teja"'])

# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_de_dup_and_sort_server():
    servertests  = pytest.importorskip("unit5_server_tests")
    servertests.test_de_dup_and_sort(de_dup_and_sort)
