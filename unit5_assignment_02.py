__author__ = 'Kalyan'

notes = '''
Again while this code passes the tests, this code is wrong as it has been modified for the sake of the tests.

Write a test case that will fail this test. Ignore infinite sequences for now.
'''

def generator_zip(seq1, seq2, *more_seqs):
    if more_seqs==():
        t=min(len(seq1),len(seq2))
        for x in range(t):
          yield (seq1[x],seq2[x])
    else:
        more_seqs = sorted(more_seqs, key=len)
        t=min(len(seq1),len(seq2),len(more_seqs[0]))
        for x in range(t):
           z=(seq1[x],seq2[x])+tuple([more_seqs[i][x] for i in range(len(more_seqs))])
           yield z


# add some test inputs that fail with the above code, then fix the above code.
def test_generator_zip_student():
    pass

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

def check_generator(gen, max_count, tuple_length):    #######max_count is number of tuples in list
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_generator_zip_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_generator_zip(generator_zip)
