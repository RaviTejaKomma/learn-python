__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
'''
1.split the sentence into words and punctuations
'''
def to_pig_latin(word):
    result=str(word)
    punctuation=""
    flag=False
    if word[-1]==',' or word[-1]=='.':
        punctuation=word[-1]
        word=word[:-1]
        result=result[:-1]
    if word[0].isupper():
       flag=True
    for char in word:
        if  char in ['a','e','i','o','u','A','E','I','O','U']:
             result=result+'ay'
             break
        else:
             result=result[1:]+result[:1].lower()
    if flag==True:
         return (result+punctuation).capitalize()
    else:
          return result+punctuation

def pig_latin(str):
    list_of_words=str.split()
    result=map(to_pig_latin,list_of_words)

    try:
       while True:
             print " ".join(result)
    except KeyboardInterrupt as ke:
           pass

if __name__ == "__main__":
    sys.argv
    pig_latin(sys.argv[1])
    #sys.exit(main())