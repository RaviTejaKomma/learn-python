__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
3. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
'''

import unit6utils
import os
def open_input_file(file, mode="rt"):
    mod_dir = unit6utils.get_module_dir()
    test_file = unit6utils.get_input_file(file)
    return open(test_file, mode)
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=unit6utils.get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)



def sort_words(source, destination):
    """
    Sort the words in the file specified by source and put them in the
    file specified by destination. The output file should have only lower
    case words, so any upper case words from source must be lowered.

    Ignore empty lines or lines starting with #
    """
    result=[]
    for line in open_input_file(source):
        if line.strip()!='' and line.strip()[0]!='#' :
            result.append(line.lower().strip())
    result.sort()
    a=result[-1]
    result=map(lambda x : x+'\n',result[:-1])
    result.append(a)
    destination1=open_temp_file(destination,"wt")
    destination1.write("".join(result))


def test_sort_words():
    source = unit6utils.get_input_file("unit6_testinput_02.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
    destination = unit6utils.get_temp_file("unit6_output_02.txt")
    sort_words(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
