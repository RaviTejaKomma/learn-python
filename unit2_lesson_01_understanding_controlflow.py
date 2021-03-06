__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
python has support for standard control flow statements similar to other languages.
iteration over sequences like list, string etc. is built into the language itself (c# has
similar features) and the loops support an else clause which is not common elsewhere.
'''

def test_if():
    value = 1
    if True:
        value = 2
    assert 2 == value

    if not True:
        value = 3
    assert 2 == value

def test_if_else():
    value = 1
    if not True:
        value = 2
    else:
        value = 3
    assert 3 == value

def test_if_elif_else():
    value = 3
    str = "str"
    if value < 0:
        str = "negative"
    elif value == 0:
        str = "zero"
    else:
        str = "positive"

    assert "positive" == str

def test_for_loop_range():
    """
    for loops are used to iterate over arbitrary sequences
    """
    nums =[]
    for x in range(1,5):
        nums.append(x)
    assert [1,2,3,4] == nums


def test_for_loop_string():

    chars = []
    for x in "engine":
        chars.append(x)
    assert ['e','n','g','i','n','e'] == chars

def test_for_loop_list():
    result = ""
    for fruit in ["orange", "banana", "apple"]:
        result += fruit
    assert "orangebananaapple" == result

def test_for_loop_list_with_enumerate():
    words = ["one", "two", "three"]
    result = []
    for p in enumerate(words):
        result.append(p)

    assert [(0, 'one'), (1, 'two'), (2, 'three')] == result
    mapping = dict(result)
    assert {0: 'one', 1: 'two', 2: 'three'} == mapping

def test_for_loop_dict():
    num_to_word = {1 : "one", 2 : "two", 3 : "three"}
    result = []
    for item in num_to_word:
        result.append(item)
    assert [1,2,3] == result

def test_while_loop():
    result = []
    while len(result) < 3:
        result.append(10)
    assert [10,10,10] == result

def test_for_loop_break():
    result = []
    for x in range(1,10):
        if x % 5 == 0:
            break
        result.append(x)

    assert [1,2,3,4] == result

def test_for_loop_continue():
    result = []
    for x in range (1, 10):
        if x % 3 == 0:
            continue
        result.append(x)
    assert [1,2,4,5,7,8] == result

def test_nested_loop_break():
    result = []
    for x in range(2):
        for y in range(1,5):
            if y%3 == 0:
                break
            result.append(x)

    assert [0,0,1,1] == result

def test_nested_loop_continue():
    result = []
    for x in range(2):
        for y in range(1,5):
            if y%3 == 0:
                continue
            result.append(x)

    assert [0,0,0,1,1,1] == result

def test_nested_loop_break_continue():
    result = []
    for x in range(3):
        for y in range(1,5):
            if y%3 == 0:
                continue
            if x%2 == 1:
                break
            result.append(x)

    assert [0,0,0,2,2,2] == result

# else on loops is not available in other common languages
def test_for_loop_else_plain():
    result = []
    for x in range(5):
        result.append(x)
        print x
    else:
        result.append(10)

    assert [0,1,2,3,4,10] == result

def test_for_loop_else_break():
    result = []
    for x in range(1,5):
        if x %3 == 0:
            break
        result.append(x)
    else:
        result.append(10)

    assert [1,2] == result

def test_for_loop_else_continue():
    result = []
    for x in range(5):
        if x %3 == 0:
            continue
        result.append(x)
    else:
        result.append(10)

    assert [1,2,4,10] == result

def test_while_loop_else():
    result = []
    x = 1
    while x in range(5):               # it is an expression evaluated to true or false not an assignment like in for loop
        result.append(x)
        x = x+1
        if x%4 == 0:
            break
    else:
        result.append(10)

    assert [1,2,3] == result


# Apply what you have learnt. Implement the method below using while, "for with else",
# if, etc.
# Don't treat this as a optimization problem, write plain brute force code :)
def get_primes(count):
    """
        Return the 1st count prime integers.
    """
    i=1
    result=[]
    while count>0:
        r=0
        i+=1
        for j in range(1,i+1):
            if i%j==0:
                r+=1
        if r==2:
            result.append(i)
            count-=1

    return result


def test_primes():
    assert [] == get_primes(0)
    assert [] == get_primes(-1)
    assert [2] == get_primes(1)
    assert [2,3,5,7,11] == get_primes(5)
    assert [2,3,5,7,11,13,17,19,23,29] == get_primes(10)

three_things_i_learnt = """
-   i have learnt about if,if-else,elif
-   i have learnt about loops and a special feature of python i.e it allows for with else
-   i have learnt about break and continue statements
"""