__author__ = 'Kalyan'

inspection_debugging = '''
Here you do not use any tools at all. The idea is to rely on the failure inputs and outputs and just use paper and pen
and work through the failing code by hand to figure out the mistake.

Basically you run the code line by line in your mind and/or paper and try to figure out the bug.

This might seem to be tedious, but this is very important as you will develop the habit of debugging code while you write
it and the quality of your code will be much better.

Majority of companies make you write code on paper/board in your face 2 face interviews, so if you lack this skill, you
will not make it.

You can identify the failing test from the pytest output. Then mentally walk through the code execution using that
input and see what could have gone wrong.
'''

import itertools

# Fix this function so that it works as expected.
# First see the output and figure out the failing input
# Then walk through it mentally and see what could have gone wrong.

def buggy_find_max(input):
    max_val = None
    for value in input:
        if max_val is None:
            max_val = value
        if max_val < value:
            max_val = value
    print max_val
    return max_val# just checking if it is correct.     ############# a return statement is expected here which is not mentioned before


def test_buggy_find_max():
    assert None == buggy_find_max([])
    assert 5 == buggy_find_max([1, 5, 3])
    assert 1 == buggy_find_max([1])


# OBSERVE THE OUTPUT ERROR, input for which it failed and walk through mentally as before.

# given a list of strings and integers, return a concatenated string
# e.g. input [1, "hello"] should return "1,hello"
# Fix this function so that it works as expected.
def buggy_join(input, sep=","):    ############## when function dont return anything it returns None object
    if input!=None:
       return sep.join(map(str,input))   ########### join dosent apply on integers so we have to convert them into strings


def test_buggy_join():
    assert "0,1,2,3,4,5" == buggy_join(range(6))
    assert "0.1.2.3.4.5" == buggy_join(range(6), ".")

    #revise the lessons if this is not clear :)
    input = list(itertools.chain(*enumerate("abc")))
    assert "0.a.1.b.2.c" == buggy_join(input, ".")

    assert None == buggy_join(None)


