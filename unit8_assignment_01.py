__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
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





def anagram_sort(source,destination):
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


if __name__ == "__main__":
    sys.argv
    source=unit6utils.get_input_file(sys.argv[1])
    destination = unit6utils.get_temp_file(sys.argv[1][:-4]+'-results.txt')
    anagram_sort(source,destination)
    # sys.exit(main())








