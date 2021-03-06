__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
import os
def open_input_file(file, mode="rt"):
    mod_dir = unit6utils.get_module_dir()
    test_file = unit6utils.get_input_file(file)
    return open(test_file, mode)
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=unit6utils.get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)


def are_anagrams(first, second):
    if first != None and second != None:
        return sorted("".join(first.lower().split())) == sorted("".join(second.lower().split()))
    else:
        return False





def anagram_sort(source, destination):
    result,anagram_sub_groups,anagram_full_groups=[],[],[]
    for line in open_input_file(source):
        if line.strip() != '' and line.strip()[0] != '#':
            result.append(line.strip())

    while result != []:
        anagram_sub_groups = [result[i] for i in range(len(result)) if are_anagrams(result[0], result[i])]
        anagram_full_groups.append(anagram_sub_groups)
        [result.remove(i) for i in anagram_sub_groups]

    [i.sort(key=lambda x: x.lower()) for i in anagram_full_groups]
    anagram_full_groups.sort(key=len, reverse=True)
    result2 = list(anagram_full_groups)
    anagram_full_groups.sort(
        cmp=lambda x, y: cmp(map(str.lower, x), map(str.lower, y)) if len(x) == len(y) else cmp(result2.index(x),
                                                                                                result2.index(y)))
    anagram_full_groups = [j for i in anagram_full_groups for j in i]
    temp = anagram_full_groups[-1]
    anagram_full_groups = map(lambda x: x + "\n", anagram_full_groups[:-1])
    anagram_full_groups.append(temp)

    f=open_temp_file(destination,"wt")
    f.write("".join(anagram_full_groups))

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
