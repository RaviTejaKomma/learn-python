__author__ = 'Ravi Teja'

from placeholders import *

notes = """string is one of the most commonly used data types, it has different
behavior than a char* in C."""



'''isinstance(object, class-or-type-or-tuple) -> bool

Return whether an object is an instance of a class or of a subclass thereof.
With a type as second argument, return whether that is the object's type.
The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
isinstance(x, A) or isinstance(x, B) or ... (etc.).'''


def test_string_type():
    assert "str" == type("Hello World").__name__
    assert True == isinstance("Hello World", str)

def test_single_quoted_strings_are_strings():
    assert True == isinstance('Hello World', str)

def test_double_quoted_strings_are_strings():
    assert True == isinstance("Hello World", str)

def test_triple_quoted_strings_are_strings():
    assert True == isinstance("""Hello World""", str)

def test_triple_single_quoted_strings_are_strings():
    assert True == isinstance('''Hello World''', str)

def test_raw_strings_are_strings():
    assert  True == isinstance(r"Hello World", str) #

def test_single_quoted_strings_can_have_double_quotes():
    first = 'The pilot said "Jump"'
    second = "The pilot said \"Jump\""  #note back slash escaping of "
    are_equal = (first == second)
    assert True == are_equal

def test_double_quoted_strings_can_have_single_quotes():
    first = "The pilot said 'Jump'"
    second = 'The pilot said \'Jump\''  #note back slash escaping of '
    are_equal = (first == second)
    assert True == are_equal

def test_triple_quoted_strings_can_have_both_single_and_double_quotes(): #DOUBTTTTTTTTTTTTTTTTTTTTTTTTTT clarified
    """ Edit tq_str to make are_equal True """
    tq_str = """ Isn't the "Hobbit" great? """                           #observe the string carefully
    dq_str = "Isn't the \"Hobbit\" great?"
    are_equal = (tq_str == dq_str)
    assert False == are_equal

def test_triple_quoted_strings_can_span_lines():     #DOUBTTTTTTTTTTTTTTTTTTT clarified
   tq_str = """Hello
World"""
   dq_str = "Hello\nWorld"   # what is the double quoted form of tq_str
   assert (tq_str == dq_str)

def test_string_len():
    assert 13 == len("Hello 'world'")
    assert 13 == len('Hello \'world\'')

def test_triple_quoted_strings_can_span_lines2(): # each line is counted as one single character
    string = """Hello
    World"""
    assert True == isinstance(string, str)
    assert 15 == len(string)                 #doubt it might be 11 but there are 4 spaces between hello and world ,it makes the length 15

def test_strings_can_be_indexed():
    string = "Hello"
    assert "H" == string[0]
    assert "e" == string[1]
    assert "l" == string[2]
    assert "l" == string[3]
    assert "o" == string[4]
    assert "o" == string[-1]  # solves the common use case to iterate from end
    assert "l" == string[-2]
    assert "l" == string[-3]
    assert "e" == string[-4]
    assert "H" == string[-5]
    assert  "H"== string[-0]  # hint -0 is 0
    assert 5 == len(string)
    try:
        out_of_bounds = string[5] #raises an error, we will revisit exceptions later
    except IndexError as ie:
        print ie                 #ie is an object of exception class
        assert True  #make this True to proceed.

def test_chars_are_strings_too():
    string = "Hello"
    first_char = string[0]
    assert "str" == type(first_char).__name__
    assert  "str"== type('a').__name__
    assert "str" == type("a").__name__

def test_strings_are_immutable():
    """ strings in python cannot be modified unlike in C """
    string = "Hello"
    try:
        string[0] = "M"                                 # in python strings are immutable . they cannot be modified
    except TypeError as te:
        print te
        assert True                                     # why we are actually using assert over here

def test_string_concat():
    assert "Hello  world" == "Hello " + " world"
    assert "Hello world" == """Hello """ + 'world'
    assert "Hello world"== 'Hello ' + "world"


def test_string_slicing():
    """ Slicing creates new strings """
    string = "Hello world"
    #with begin : end
    assert ""== string[0:0]
    assert "He" == string[0:2]
    assert "ello"== string[1:5]
    assert "ello worl"== string[1:-1]
    assert "llo wor" == string[2:-2]

    #with :end, note usage of negative indices as well.
    assert "" == string[:0]
    assert "Hell" == string[:4]
    assert "Hello worl"== string[:-1]

    #with begin:
    assert "Hello world" == string[0:]
    assert "o world" == string[4:]
    assert "d"== string[-1:]

    #observe the invariant
    assert "Hello world" == string[:0] + string[0:]
    assert "Hello world" == string[:1] + string[1:]
    assert "Hello world" == string[:2] + string[2:]
    assert "Hello world"== string[:3] + string[3:]


def test_string_repeat():
    assert "Hello"+"Hello"+"Hello" == "Hello" * 3
    assert 12== len("Hello " * 2)

def test_string_combine():
    """
    Use slicing to pass the assert.
    """
    hello = "Hello World"
    bye = "Goodbye moon"
    assert  bye[:7] + hello[5:]  == "Goodbye World"

def test_string_formatting():                             # learner is assigned an index 0 , format({0],{1}...............)
    greeting = "Hello '{0}'".format("learner")
    assert "Hello 'learner'" == greeting

    truth = "{1} plus {1} makes {0}".format("two","one")
    assert truth == "one plus one makes two"

    stmt = "{name} is {age} years old".format(name="Ravi", age=25)
    assert "Ravi is 25 years old" == stmt

def test_string_membership():                    # take a note of this
    assert  True or 'c' == 'c' in 'apple'            #is there a precedence issue here or something else?
    assert 'a'== 'a' in 'apple'
    assert 'app' == 'app' in 'apple'


#Now apply what you have learnt above.
def rotate_right(input, count):
    """
    write a single line of code using what you have learnt in this lesson - slicing and concat
    assume 0 <= count <= len(input)
    """
    return input[-count:]+input[:-count] # replace __ with the code

def test_rotate():
    assert 'hello' == rotate_right("hello", 0)
    assert 'ohell' == rotate_right("hello", 1)
    assert 'lohel' == rotate_right("hello", 2)
    assert 'llohe' == rotate_right("hello", 3)
    assert 'elloh' == rotate_right("hello", 4)
    assert 'hello' == rotate_right("hello", 5)


three_things_i_learnt = """
-
-
-
"""
