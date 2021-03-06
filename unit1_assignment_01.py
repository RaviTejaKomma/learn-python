__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
Fill up each of these methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

Idea is for you to refer to online documentation and get your work done.

All of these functions require use of the builtin functions documented at
http://docs.python.org/2/library/functions.html

Your job is to see which ones apply and invoke them. Most of the methods require
writing 1 or 2 lines of code.

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.

I repeat, No control statements please even if you already know python!

Notes:

1. This assignment will encourage top-down declarative thinking in you. You are all familiar with bottoms-up thinking,
   this is another important habit to develop. You need both.

2. This will help you to think in terms of problem decomposition into smaller problems that are usually
   done for you by python or you solve the smaller problems further till you reach sub-problems that python does for you.

3. Read the input constraints carefully, I purposely constrain inputs for this learning assignment.

4. If you think a particular builtin will be useful, play with it in the console and see how it works.

5. Reading material:
    http://latentflip.com/imperative-vs-declarative (read once before and after doing the exercises).
'''


def get_odds_desc(count):
    """
     This method returns a list of the first 'count' odd numbers in descending
     order. e.g count = 3 should return [5,3,1]
    """
    return list(reversed(range(1,count*2,2)))

def test_odds_list():
    assert [1] == get_odds_desc(1)
    assert [] == get_odds_desc(0)
    assert [5,3,1] == get_odds_desc(3)
    assert [9,7,5,3,1] == get_odds_desc(5)


def get_multiples_desc(number, count):
    """
    return the first count multiples of number in desc order in a list.
    e.g call with input (3,2) returns [6,3]
    call with input(5,3) returns [15,10, 5]

    Hint: one line of code, use a builtin function we have already seen in the lists lesson.
    """
    return list(reversed(range(number,(number*count)+1,number)))


# fill up the above functions so that these tests pass.
def test_get_multiples_desc():
    assert [6,3] == get_multiples_desc(3,2)
    assert [15, 10, 5] == get_multiples_desc(5,3)
    assert [] == get_multiples_desc(6, 0)
    assert [3,2,1] == get_multiples_desc(1, 3)



def ascii_distance(first, second):
    """
    returns the positive distance between the ascii values of input characters
    assume: inputs are valid single letters
    e.g. inputs ("a", "b") should return 1,
        inputs ("b", "a") should return 1 too (postive distance)
    """
    return  abs(ord(first)-ord(second))# use 2 builtin functions to get your work done.

def test_ascii_distance():
    assert 1 == ascii_distance("a", "b")
    assert 1 == ascii_distance("b", "a")
    assert 1 == ascii_distance("B", "A")
    assert 32 == ascii_distance("A", "a")
    assert 31 == ascii_distance("B", "a")

def get_binary(number):
    """
    Return the binary string of number (>=0) without 0b prefix.
    For e.g 5 returns "101", 20 returns "10100" etc.
    """
    return bin(number)[2:] # use a builtin and slice the result ...

def test_get_binary():
    assert "100" == get_binary(4)
    assert "11111111" == get_binary(255)
    assert "0" == get_binary(0)

def get_min_max(input):
    """
    returns the min, max elements in the input as a tuple.
    """
    return tuple(sorted(input)[:1]+sorted(input)[-1:])


def test_min_max():
    assert (2,10) == get_min_max([2,3,5,10])
    assert (2,2) == get_min_max([2,2,2])
    assert (2,5) == get_min_max((5,2,2,2))
    assert (5,5) == get_min_max([5])


def base36_to_binary(input):
    """
    returns a specified string in base 36 as a string in binary. see tests for expected results
    Hint: use a couple of builtins and slicing to make this happen.
    """
    return bin(int(input,36))[2:]

def test_base36_to_binary():
    assert "1010" == base36_to_binary("A")
    assert "100011" == base36_to_binary("Z")
    assert "100100" == base36_to_binary("10")
    assert "101110011" == base36_to_binary("AB")


def count_binary_ones(number):
    """
    Returns the number of 1s in the binary representation of number (>=0)
    For e.g 5 returns 2 (101 has 2 1's), 21 returns 3 ("10101")
    """
    # Use only builtins to get this done. No control statements plz
    return bin(number)[2:].count("1")

def test_count_binary_ones():
    assert 8 == count_binary_ones(0xFF)
    assert 0 == count_binary_ones(0)
    assert 3 == count_binary_ones(0b101010)
    assert 4 == count_binary_ones(15)
