__author__ = 'RaviTeja'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    temp=number
    remainder=0
    result = ""
    if (2<=base<=36) and (type(number).__name__=="int"):
       while abs(number) != 0:
             remainder = abs(number) % base
             if remainder > 9:
                result = result + chr(remainder - 10 + 65)
             else:
                result = result + str(remainder)
             number = abs(number) / base


       if temp < 0:
           return "-" + result[::-1]
       else:
            return result[::-1]


def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        raise ValueError
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert(10, 40)
        raise ValueError
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print ve

    try:
        convert("100", 10)
        raise TypeError
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te

    try:
        convert(None, 10)
        raise TypeError
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print te


    try:
        convert(100, "10")
        raise TypeError
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print te