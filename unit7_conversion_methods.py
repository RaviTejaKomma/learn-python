__author__ = 'Kalyan'

notes = '''
This is a sample program that you can use to try out and learn the 3 methods of profiling.
Given below are 4 ways of solving a problem of getting a comma separated string of numbers. e.g. 0,1,2,3

The assignments are about profiling these methods and determining relative performance of each approach
as you vary count.
'''

import collections

#return a string "0,1,...,count-1"

def numbers_string1(count):
    result = ""
    for i in range(count-1):
        result += str(i) + ","
    if count > 0:
        result += str(count-1)
    return result

def numbers_string2(count):
    nums = range(count)
    num_strings = map(str, nums)
    return ",".join(num_strings)

def numbers_string3(count):
    num_strings = [str(i) for i in range(count)]
    return ",".join(num_strings)

def num_strings4(count):
    num_strings = [str(i) for i in xrange(count)]
    return ",".join(num_strings)

