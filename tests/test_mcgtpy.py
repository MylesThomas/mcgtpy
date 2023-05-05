# Import methods from our Modules
from mcgtpy.my_stats import print_stats
from mcgtpy.helper_functions import columns_janitor

# Print stats (we don't need this necessarily ...)
print_stats()

# Tests to make sure columns_janitor() is on point
def test_1():
    input = ['  MYleS  __    _', '  _ chRistian______ George___', '____ tHomas ']
    actual = columns_janitor(input)
    expected = ['myles', 'christian_george', 'thomas']
    assert actual == expected

def test_2():
    input = ['Hey', "Hello"]
    actual = columns_janitor(input)
    expected = ["hey", "hello"]
    assert actual == expected

def test_3():
    input = ['HEY    __  ', "     A   ___  b ___ C "]
    actual = columns_janitor(input)
    expected = ["hey", "a_b_c"]
    assert actual == expected

def test_4():
    input = ['__myles___  ___', '__CHRISTIAN   gEORGE  ', '  __ THomAS _  _   ']
    actual = columns_janitor(inputs)
    expected = ['myles', 'christian_george', 'thomas']
    assert actual == expected