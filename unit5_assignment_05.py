__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.

def prune_either_or(sentence):
    if sentence==None:
        return None
    blah,something="",""
    index1 = sentence.find("either")
    index2 = sentence.find("or")
    if "either" in sentence and "or" in sentence and index1 < index2 and index1!=0 and index2!=len(sentence)-2 :
       flag1= sentence[sentence.find("either")+6]==' ' and sentence[sentence.find("either")-1]==' '
       flag2 = sentence[sentence.find("or") + 2] == ' ' and sentence[sentence.find("or") - 1] == ' '
       if  flag1 and flag2:
           blah = sentence[:sentence.find("either")]
           something = sentence[sentence.find("either")+6:sentence.find("or")]
           blah= blah.strip()
           something=something.strip()
           sentence=blah+" "+something
           return sentence
       else:
           return sentence
    else:
        return sentence
def test_prune_either_or_student():
    assert "we could go to a movie"==prune_either_or("we could either go to a movie or a hotel")
    assert "we could either go to a movie a hotel" == prune_either_or("we could either go to a movie a hotel")
    assert "we could go to a movie or a hotel" == prune_either_or("we could go to a movie or a hotel")
    assert "we could go to a movie a hotel " == prune_either_or("we could go to a movie a hotel ")
    assert "either i accompany you to your room or i wait here" == prune_either_or("either i accompany you to your room or i wait here")
    assert "either or"==prune_either_or("either or")
    assert "neither this or that"==prune_either_or("neither this or that")
    assert " either or" == prune_either_or(" either or")
    assert "Two mythical cities eitheron and oregon" == prune_either_or("Two mythical cities eitheron and oregon")
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
