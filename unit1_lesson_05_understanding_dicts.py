__author__ = 'Ravi Teja'

from placeholders import *

notes = '''
dicts are unordered sets of key value pairs which facilitate fast lookups by key.
'''

def test_dictionary_type():
    test_dict = {1 : "one"}   # note the new syntax
    assert "dict" == type(test_dict).__name__

def test_dictionary_empty():
    empty_dict_1 = {}            ######### empty  dictionary
    assert True == isinstance(empty_dict_1, dict)

    empty_dict_2 = dict() # another way of creating empty dict#########################
    assert 0 == len(empty_dict_2)

    assert empty_dict_1 == empty_dict_2

def test_dictionary_create():
    dict_1 = { 1 : "one", 2 : "two" }                     #dict={key:value}
    assert True== isinstance(dict_1, dict)

    #init from a sequence of tuple pairs, useful in many cases.
    dict_2 = dict([(1, "one"), (2, "two")])
    assert  'one'== dict_2[1]
    assert 'two'== dict_2[2]

def test_dictionary_length():
    word_to_digit = { "one" : 1, "two" : 2}
    assert 2 == len(word_to_digit) #note that a key value pair is treated as one item

def test_dictionary_is_indexed_by_key():
    word_to_digit = { "one" : 1, "two" : 2}
    assert 1 == word_to_digit["one"]
    assert 2 == word_to_digit["two"]

    try:
        word_to_digit[1]
    except Exception as ex:
    #Note that numeric indicies don't mean much like in case of lists and tuples
        print ex
        assert True

def test_dictionary_is_mutable():
    word_to_digit = { "one" : 1, "two" : 2}    ######### dictionaries are not ordered they can be arranged in any way

    word_to_digit["three"] = 3
    assert {"one" : 1, "two" : 2 , "three" : 3} == word_to_digit

    del word_to_digit["one"]
    assert {"two" : 2 , "three" : 3} == word_to_digit

    word_to_digit["one"] = 10
    assert {"two" : 2 , "three" : 3,"one" : 10} == word_to_digit

def test_dictionary_is_unordered():
    dict1 = { 'one': 1, 'two': 2 }
    dict2 = { 'two': 2, 'one': 1}

    equal = (dict1 == dict2)
    assert True == equal # True or False?

def test_dictionary_keys_and_values():
    word_to_digit = { "one" : 1, "two" : 2}   ############  keys()    values() are two functions
    assert 2 == len(word_to_digit.keys())
    assert 2 == len(word_to_digit.values())
    keys = word_to_digit.keys()
    #sort to get a deterministic order
    keys.sort()
    assert ['one', 'two'] == keys             ############# sorted in ascending order
    values = word_to_digit.values()
    values.sort()
    assert [1,2] == values

def test_dictionary_contains():
    word_to_digit = { "one" : 1, "two" : 2}

    assert True== ("one" in word_to_digit)
    assert True== ("two" in word_to_digit)

    assert True == ("one" in word_to_digit.keys())
    assert True == ("two" in word_to_digit.keys())

    assert False == (1 in word_to_digit) ####################### take a note ------ we search the value using the key not value
    assert False== (2 in word_to_digit)

    assert True == (1 in word_to_digit.values())
    assert True == (2 in word_to_digit.values())

def test_valid_dictionary_keys():
    test_dict = {}
    test_dict[1] = 1
    test_dict["one"] = "string"
    try:
        key = []                                       ########## key can not be a NULL value
        test_dict[key] = "list"
    except TypeError as te:
        print te  #observe the error message.
        assert True

    try:
        key = (1,2)
        test_dict[key] = "tuple with immutable elements"           ###### key can be a TUPLE ------key can be anything
    except TypeError as te:
        print te
        assert False # do we reach here?                          ######### control will not reach here assert can be true or false

    try:
        key = (1, [])
        test_dict[key] = "tuple with mutable element"
    except TypeError as te:
        print te
        assert True #do we reach here?

    assert {1:1,(1,2):"tuple with immutable elements" ,"one":"string"} == test_dict


# Apply what you have learnt in this lesson.
# Hint: See help(zip) in console or in online documentation
def make_dict(keys, values):
    """
    Returns a dictionary that maps keys to values correspondingly.
    Assume inputs are of same length.
    """
    return dict(zip(keys,values)) # write a single line of code to create the dict.
    # zip function pairs up the corresponding elements in two lists and returns another list
import string

def test_make_dict():
    #map digits to their successors
    result = make_dict(range(10), range(1,11))
    for key, value in result.items():
        assert key + 1 == value

    # map numerical digits to their string values
    result = make_dict(range(10), string.digits)
    for key, value in result.items():
        assert value == str(key)
        assert key == int(value)


three_things_i_learnt = """
-
-
-
"""

notes2= '''
It is  good to understand how dictionaries are generally implemented under the hood.
Go through the the entire thread at
http://stackoverflow.com/questions/730620/how-does-a-hash-table-work
and discuss in the group if required.
'''